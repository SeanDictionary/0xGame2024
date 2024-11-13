const { MongoClient } = require('mongodb');

const uri = process.env.MONGODB_URI || "mongodb://127.0.0.1:27017/";
const client = new MongoClient(uri);

async function init() {
    const db = client.db('next-db');
    const collection = db.collection('frameworks');

    await collection.insertMany([
        {
            id: 0,
            name: "flag",
            description: process.env.FLAG || "flag{test}",
        },
        {
            id: 1,
            name: "Next.js",
            description: "The React Framework for the Web",
        },
        {
            id: 2,
            name: "Nuxt.js",
            description: "The Intuitive Vue Framework",
        },
        {
            id: 3,
            name: "React",
            description: "The library for web and native user interfaces"
        },
        {
            id: 4,
            name: "Vue.js",
            description: "The Progressive JavaScript Framework"
        }
    ]);

    await client.close();
}

init();