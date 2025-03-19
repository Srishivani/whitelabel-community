from datetime import datetime, UTC
from typing import List
from .db.base import Database

class CommunityService:
    def __init__(self, db: Database):
        self.db = db

    async def create_community(self, name: str, owner_id: str, description: str) -> dict:
        community = {
            "name": name,
            "owner_id": owner_id,
            "description": description,
            "members": [{"user_id": owner_id, "role": "admin"}],
            "created_at": datetime.now(UTC),
            "settings": {"private": False}
        }
        community_id = await self.db.insert_one("communities", community)
        return {"id": community_id, **community}

    async def add_member(self, community_id: str, user_id: str, role: str = "member") -> bool:
        return await self.db.update_one(
            "communities",
            {"_id": community_id},
            {"$push": {"members": {"user_id": user_id, "role": role}}}
        )

    async def get_user_communities(self, user_id: str) -> List[dict]:
        return await self.db.find_many(
            "communities",
            {"members": {"$elemMatch": {"user_id": user_id}}}
        )
