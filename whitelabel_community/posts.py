from datetime import datetime, UTC
from typing import List, Optional
from .db.base import Database

class PostService:
    def __init__(self, db: Database):
        self.db = db

    async def create_post(self, community_id: str, author_id: str, title: str, content: str) -> dict:
        post = {
            "community_id": community_id,
            "author_id": author_id,
            "title": title,
            "content": content,
            "created_at": datetime.now(UTC),
            "likes": 0,
            "comments": []
        }
        post_id = await self.db.insert_one("posts", post)
        return {"id": post_id, **post}

    async def add_comment(self, post_id: str, author_id: str, content: str) -> bool:
        comment = {
            "author_id": author_id,
            "content": content,
            "created_at": datetime.now(UTC)
        }
        return await self.db.update_one(
            "posts",
            {"_id": post_id},
            {"$push": {"comments": comment}}
        )

    async def get_community_posts(self, community_id: str) -> List[dict]:
        return await self.db.find_many("posts", {"community_id": community_id})
