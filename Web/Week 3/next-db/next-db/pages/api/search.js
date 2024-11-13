import { MongoClient } from 'mongodb';

const uri = process.env.MONGODB_URI || "mongodb://127.0.0.1:27017/";
const client = new MongoClient(uri);

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ message: 'Method not allowed' });
  }

  const { name } = req.body;
  if (!name) {
    return res.status(500).json({ message: 'Name is required' });
  }

  if (name === "flag") {
    return res.status(500).json({ message: 'You are not allowed to search for the flag' });
  }

  try {
    const db = client.db('next-db');
    const collection = db.collection('frameworks');
    const results = await collection.find({
      $or: [
        { name },
        {
          $and: [
            { description: { $regex: name.toString(), $options: 'i' } },
            { description: { $ne: process.env.FLAG || "flag{test}" } }
          ]
        }
      ]
    }).toArray();

    res.status(200).json(results);
  } catch (error) {
    console.error('Database query error:', error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
}
