use actix_files::NamedFile;
use actix_web::{get, middleware::Logger, post, web, App, HttpServer, Responder};
use futures_core::future::BoxFuture;
use futures_util::FutureExt;
use mysql_async::{
    prelude::{GlobalHandler, Queryable},
    Conn, InfileData, LocalInfileError, OptsBuilder,
};
use serde::Deserialize;
use tokio::fs::File;
use tokio_util::io::ReaderStream;

struct UnsafeFsHandler;

impl GlobalHandler for UnsafeFsHandler {
    fn handle(&self, file_name: &[u8]) -> BoxFuture<'static, Result<InfileData, LocalInfileError>> {
        let path = String::from_utf8_lossy(file_name).to_string();
        async move {
            println!("reading file: {}", path);
            let file = File::open(path).await?;
            Ok(Box::pin(ReaderStream::new(file)) as InfileData)
        }
        .boxed()
    }
}

#[derive(Deserialize)]
struct ConnInfo {
    host: String,
    port: u16,
    user: String,
    pass: String,
    db: String,
    query: String,
}

#[get("/")]
async fn index() -> impl Responder {
    NamedFile::open("./public/index.html")
}

#[post("/connect")]
async fn connect(info: web::Json<ConnInfo>) -> Result<impl Responder, Box<dyn std::error::Error>> {
    let conn_info = info.into_inner();

    let opts = OptsBuilder::default()
        .ip_or_hostname(conn_info.host)
        .tcp_port(conn_info.port)
        .user(Some(conn_info.user))
        .pass(Some(conn_info.pass))
        .db_name(Some(conn_info.db))
        .local_infile_handler(Some(UnsafeFsHandler));

    let mut conn = Conn::new(opts).await?;
    let v: String = conn.query_first(conn_info.query).await?.unwrap();

    Ok(v)
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    env_logger::init();

    HttpServer::new(|| {
        App::new()
            .wrap(Logger::new(
                r#"%{r}a "%r" %s %b "%{Referer}i" "%{User-Agent}i" %T"#,
            ))
            .service(index)
            .service(connect)
    })
    .bind(("0.0.0.0", 8000))?
    .run()
    .await
}
