use std::{env, vec};

use actix_session::{storage::CookieSessionStore, Session, SessionMiddleware};
use actix_web::{cookie::Key, get, middleware::Logger, web, App, HttpServer, Result};
use lazy_static::lazy_static;
use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
struct Goods {
    name: String,
    price: u32,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
struct Hold {
    goods: Goods,
    inventory: u32,
}

#[derive(Debug, Serialize, Deserialize)]
struct User {
    holds: Vec<Hold>,
    balance: i32,
}

lazy_static! {
    static ref GOODS_LIST: Vec<Goods> = vec![
        Goods {
            name: String::from("actix-web"),
            price: 10
        },
        Goods {
            name: String::from("axum"),
            price: 20
        },
        Goods {
            name: String::from("reqwest"),
            price: 50
        },
        Goods {
            name: String::from("tokio"),
            price: 100,
        },
        Goods {
            name: String::from("flag"),
            price: 1_000_000_000
        },
    ];
}

#[get("/")]
async fn index(session: Session) -> Result<String> {
    match session.get::<User>("user")? {
        Some(user) => Ok(format!(
            "balance: {}, holds: {:?}",
            user.balance, user.holds
        )),
        None => {
            let user = User {
                holds: Vec::new(),
                balance: 1_000,
            };
            session.insert("user", user)?;
            Ok("Welcome to cargo shop! your initial balance is 1000".to_string())
        }
    }
}

#[get("/purchase/{name}/{count}")]
async fn purchase(info: web::Path<(String, u32)>, session: Session) -> Result<String> {
    let Some(mut user) = session.get::<User>("user")? else {
        return Ok("user not found".to_string());
    };

    let (name, count) = info.into_inner();

    let Some(goods) = GOODS_LIST.iter().find(|v| v.name == name) else {
        return Ok("goods not found".to_string());
    };

    let costs = (goods.price * count) as i32;

    if costs <= user.balance {
        user.balance -= costs;

        if let Some(hold) = user.holds.iter_mut().find(|v| v.goods.name == goods.name) {
            hold.inventory += count;
        } else {
            user.holds.push(Hold {
                goods: goods.clone(),
                inventory: count,
            });
        }

        session.insert("user", user)?;
        Ok(format!("purchase {} x {} success", name, count))
    } else {
        Ok(format!("you don't have enough balance"))
    }
}

#[get("/sell/{name}/{count}")]
async fn sell(info: web::Path<(String, u32)>, session: Session) -> Result<String> {
    let Some(mut user) = session.get::<User>("user")? else {
        return Ok("user not found".to_string());
    };

    let (name, count) = info.into_inner();

    let Some(hold) = user.holds.iter_mut().find(|v| v.goods.name == name) else {
        return Ok("goods not found".to_string());
    };

    if count > hold.inventory {
        return Ok("you don't have enough goods".to_string());
    }

    let earns = (hold.goods.price * count) as i32;
    user.balance += earns;
    hold.inventory -= count;

    session.insert("user", user)?;
    Ok(format!("sell {} x {} success", name, count))
}

#[get("/flag")]
async fn flag(session: Session) -> Result<String> {
    let Some(user) = session.get::<User>("user")? else {
        return Ok("user not found".to_string());
    };

    let Some(flag) = user.holds.iter().find(|v| v.goods.name == "flag") else {
        return Ok("flag goods not found".to_string());
    };

    if flag.inventory > 0 {
        Ok(env::var("FLAG").unwrap_or("flag{test}".to_string()))
    } else {
        Ok("you need to buy the `flag` goods to get flag".to_string())
    }
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    let secret_key = Key::generate();

    env_logger::init();

    HttpServer::new(move || {
        App::new()
            .wrap(Logger::new(
                r#"%{r}a "%r" %s %b "%{Referer}i" "%{User-Agent}i" %T"#,
            ))
            .wrap(
                SessionMiddleware::builder(CookieSessionStore::default(), secret_key.clone())
                    .cookie_secure(false)
                    .build(),
            )
            .service(index)
            .service(purchase)
            .service(sell)
            .service(flag)
    })
    .bind(("0.0.0.0", 8000))?
    .run()
    .await
}
