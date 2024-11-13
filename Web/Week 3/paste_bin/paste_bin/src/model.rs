use serde::{Deserialize, Serialize};

#[derive(Clone, Serialize, Deserialize)]
pub struct Paste {
    pub id: String,
    pub content: String,
}

#[derive(Serialize, Deserialize)]
pub struct PasteContent {
    pub content: String,
}

#[derive(Serialize, Deserialize)]
pub struct PasteId {
    pub id: String,
}

#[derive(Serialize, Deserialize)]
pub struct Message {
    pub msg: String,
}
