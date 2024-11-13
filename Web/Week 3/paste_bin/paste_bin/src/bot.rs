use std::{env, time::Duration};

use fantoccini::ClientBuilder;

pub async fn visit_paste(id: &str) -> Result<(), Box<dyn std::error::Error>> {
    let flag: String = env::var("FLAG").unwrap_or("flag{test}".to_string());
    let js = format!("localStorage.setItem('flag', '{}');", flag);

    let mut caps = serde_json::map::Map::new();
    let opts = serde_json::json!({
        "args": [
            "--headless",
            "--no-sandbox",
            "--disable-gpu",
            "--disable-dev-shm-usage",
            "--remote-debugging-port=9222"
        ],
    });
    caps.insert("goog:chromeOptions".to_string(), opts);

    let c = ClientBuilder::native()
        .capabilities(caps)
        .connect("http://bot:4444")
        .await?;

    println!("visiting home page");
    c.goto("http://web:8000/").await?;
    c.execute(&js, vec![]).await?;

    println!("visiting paste: {}", id);
    let view_url = "http://web:8000/view?id=".to_string() + id;
    c.goto(&view_url).await?;

    println!("bot will sleep for 10s");
    tokio::time::sleep(Duration::from_secs(10)).await;

    println!("visited paste: {} success", id);
    c.close().await?;

    Ok(())
}
