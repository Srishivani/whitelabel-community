from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

class Database(ABC):
    @abstractmethod
    async def find_one(self, collection: str, query: Dict) -> Optional[Dict]:
        pass

    @abstractmethod
    async def find_many(self, collection: str, query: Dict) -> List[Dict]:
        pass

    @abstractmethod
    async def insert_one(self, collection: str, document: Dict) -> Any:
        pass

    @abstractmethod
    async def update_one(self, collection: str, query: Dict, update: Dict) -> bool:
        pass

    @abstractmethod
    async def delete_one(self, collection: str, query: Dict) -> bool:
        pass
