import pytest
import warnings
from pytest_asyncio import fixture
from typing import Dict, List, Optional
from whitelabel_community.db.base import Database

# Suppress specific UTC warning from jose library
warnings.filterwarnings(
    "ignore",
    message="datetime.datetime.utcnow\(\) is deprecated",
    category=DeprecationWarning,
    module="jose.jwt"
)

class MockDatabase(Database):
    def __init__(self):
        self.data = {}
        
    async def find_one(self, collection: str, query: Dict) -> Optional[Dict]:
        return next((item for item in self.data.get(collection, []) 
                    if all(item.get(k) == v for k, v in query.items())), None)
        
    async def find_many(self, collection: str, query: Dict) -> List[Dict]:
        results = []
        for item in self.data.get(collection, []):
            matches = True
            for key, value in query.items():
                if isinstance(value, dict) and '$elemMatch' in value:
                    elem_match = value['$elemMatch']
                    if not any(
                        all(elem.get(k) == v for k, v in elem_match.items())
                        for elem in item.get(key, [])
                    ):
                        matches = False
                        break
                elif item.get(key) != value:
                    matches = False
                    break
            if matches:
                results.append(item)
        return results
        
    async def insert_one(self, collection: str, document: Dict) -> str:
        if collection not in self.data:
            self.data[collection] = []
        document['_id'] = str(len(self.data[collection]))
        self.data[collection].append(document)
        return document['_id']
        
    async def update_one(self, collection: str, query: Dict, update: Dict) -> bool:
        for item in self.data.get(collection, []):
            if all(item.get(k) == v for k, v in query.items()):
                if '$set' in update:
                    item.update(update['$set'])
                if '$push' in update:
                    for field, value in update['$push'].items():
                        if field not in item:
                            item[field] = []
                        item[field].append(value)
                return True
        return False
        
    async def delete_one(self, collection: str, query: Dict) -> bool:
        items = self.data.get(collection, [])
        initial_len = len(items)
        self.data[collection] = [item for item in items 
                               if not all(item.get(k) == v for k, v in query.items())]
        return len(self.data[collection]) < initial_len

@fixture
async def mock_db():
    return MockDatabase()
