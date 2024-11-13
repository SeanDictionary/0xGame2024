use std::{fs, path::Path};

use actix_web::{
    middleware::Logger,
    web::{self},
    App, HttpServer,
};
use paste_bin::{db, route};
use r2d2::Pool;
use r2d2_sqlite::SqliteConnectionManager;

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    let db_file = "db/file.db";

    let p = Path::new(db_file);
    if p.exists() {
        fs::remove_file(p).unwrap();
    }

    let manager = SqliteConnectionManager::file(db_file);
    let pool = Pool::new(manager).unwrap();
    let data = web::Data::new(pool);

    db::init(&data);
    env_logger::init();

    HttpServer::new(move || {
        App::new()
            .wrap(Logger::new(
                r#"%{r}a "%r" %s %b "%{Referer}i" "%{User-Agent}i" %T"#,
            ))
            .app_data(web::Data::clone(&data))
            .service(route::index)
            .service(route::view)
            .service(route::report)
            .service(route::view_paste)
            .service(route::post_paste)
            .service(route::delete_paste)
            .service(route::do_report)
            .service(actix_files::Files::new("/static", "./static/"))
    })
    .bind(("0.0.0.0", 8000))?
    .run()
    .await
}
