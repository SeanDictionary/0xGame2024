use r2d2::{Pool, PooledConnection};
use r2d2_sqlite::SqliteConnectionManager;
use rusqlite::params;
use uuid::Uuid;

use crate::model::Paste;

pub fn init(pool: &Pool<SqliteConnectionManager>) {
    let conn = pool.get().unwrap();
    conn.execute("CREATE TABLE pastes(id TEXT PRIMARY KEY, content TEXT)", [])
        .unwrap();
}

pub fn select(
    conn: &PooledConnection<SqliteConnectionManager>,
    id: &str,
) -> Result<Paste, rusqlite::Error> {
    let mut stmt = conn.prepare("SELECT id, content FROM pastes WHERE id = ?")?;
    let paste = stmt.query_row(params![id], |row| {
        Ok(Paste {
            id: row.get(0)?,
            content: row.get(1)?,
        })
    });

    paste
}

pub fn insert(
    conn: &PooledConnection<SqliteConnectionManager>,
    content: &str,
) -> Result<String, rusqlite::Error> {
    let id = Uuid::new_v4().to_string();
    conn.execute("INSERT INTO pastes VALUES(?, ?)", params![id, content])?;

    Ok(id)
}

pub fn delete(
    conn: &PooledConnection<SqliteConnectionManager>,
    id: &str,
) -> Result<(), rusqlite::Error> {
    conn.execute("DELETE FROM pastes WHERE id = ?", params![id])?;

    Ok(())
}
