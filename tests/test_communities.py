import pytest
from whitelabel_community.communities import CommunityService

@pytest.mark.asyncio
async def test_community_operations(mock_db):
    community_service = CommunityService(mock_db)
    
    # Test community creation
    community = await community_service.create_community(
        name="Test Community",
        owner_id="user123",
        description="Test Description"
    )
    assert community["name"] == "Test Community"
    assert community["owner_id"] == "user123"
    
    # Test adding member
    success = await community_service.add_member(
        community_id=community["id"],
        user_id="user456",
        role="member"
    )
    assert success is True
    
    # Test getting user communities
    communities = await community_service.get_user_communities("user123")
    assert len(communities) == 1
    assert communities[0]["name"] == "Test Community"
