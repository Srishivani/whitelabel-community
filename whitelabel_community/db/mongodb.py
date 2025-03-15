from motor.motor_asyncio import AsyncIOMotorClient
from typing import Any, Dict, List, Optional
from .base import Database

class MongoDatabase(Database):
    def __init__(self, connection_url: str):
        self.client = AsyncIOMotorClient(connection_url)
        self.db = self.client.get_default_database()

    async def find_one(self, collection: str, query: Dict) -> Optional[Dict]:
        return await self.db[collection].find_one(query)

    async def find_many(self, collection: str, query: Dict) -> List[Dict]:
        return await self.db[collection].find(query).to_list(length=None)

    async def insert_one(self, collection: str, document: Dict) -> Any:
        result = await self.db[collection].insert_one(document)
        return result.inserted_id

    async def update_one(self, collection: str, query: Dict, update: Dict) -> bool:
        result = await self.db[collection].update_one(query, {"$set": update})
        return result.modified_count > 0

    async def delete_one(self, collection: str, query: Dict) -> bool:
        result = await self.db[collection].delete_one(query)
        return result.deleted_count > 0
