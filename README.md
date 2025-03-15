# Whitelabel Community Platform

A flexible and scalable backend for building community platforms using FastAPI and MongoDB.

## Features

- 🔐 JWT-based authentication
- 👥 Community management with roles and permissions  
- ✍️ Post and comment functionality
- 🗄️ Async MongoDB integration
- ✅ 84% test coverage

## Quick Start

```python
from whitelabel_community import CommunityService
from whitelabel_community.db import MongoDatabase

# Initialize database
db = MongoDatabase("mongodb://localhost:27017/mydb")

# Create community service
community_service = CommunityService(db)

# Create a community
community = await community_service.create_community(
    name="My Community",
    owner_id="user123",
    description="A test community"
)
```

## Installation

```bash
pip install git+https://github.com/Srishivani/whitelabel_community.git
```

## Development

1. Clone the repository
2. Install dependencies: `pip install -e ".[dev,test]"`
3. Run tests: `pytest`

## License

MIT License
