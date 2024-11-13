use actix_files::NamedFile;
use actix_web::{
    get, post,
    web::{self},
    Responder,
};
use r2d2::Pool;
use r2d2_sqlite::SqliteConnectionManager;
use uuid::Uuid;

use crate::{
    bot, db,
    model::{Message, PasteContent, PasteId},
};

#[get("/")]
async fn index() -> impl Responder {
    NamedFile::open("./public/index.html")
}

#[get("/view")]
async fn view() -> impl Responder {
    NamedFile::open("./public/view.html")
}

#[get("/report")]
async fn report() -> impl Responder {
    NamedFile::open("./public/report.html")
}

#[post("/api/view/{id}")]
async fn view_paste(
    info: web::Path<String>,
    data: web::Data<Pool<SqliteConnectionManager>>,
) -> Result<impl Responder, Box<dyn std::error::Error>> {
    let pool = data.clone();
    let conn = pool.get()?;

    let id = info.into_inner();
    Uuid::parse_str(&id)?;
    let paste = db::select(&conn, &id)?;

    Ok(web::Json(paste))
}

#[post("/api/paste")]
async fn post_paste(
    form: web::Form<PasteContent>,
    data: web::Data<Pool<SqliteConnectionManager>>,
) -> Result<impl Responder, Box<dyn std::error::Error>> {
    let pool = data.clone();
    let conn = pool.get()?;

    let content = form.into_inner().content;
    let id = db::insert(&conn, &content)?;

    Ok(web::Json(PasteId { id }))
}

#[post("/api/delete/{id}")]
async fn delete_paste(
    info: web::Path<String>,
    data: web::Data<Pool<SqliteConnectionManager>>,
) -> Result<impl Responder, Box<dyn std::error::Error>> {
    let pool = data.clone();
    let conn = pool.get()?;

    let id = info.into_inner();
    Uuid::parse_str(&id)?;
    db::delete(&conn, &id)?;

    Ok(web::Json(Message {
        msg: "delete paste success".to_string(),
    }))
}

#[post("/api/report/{id}")]
async fn do_report(info: web::Path<String>) -> Result<impl Responder, Box<dyn std::error::Error>> {
    let id = info.into_inner();
    Uuid::parse_str(&id)?;
    tokio::task::spawn(async move { bot::visit_paste(&id).await.unwrap() });

    Ok(web::Json(Message {
        msg: "bot will visit the url soon".to_string(),
    }))
}
