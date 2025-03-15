import pytest
from whitelabel_community.posts import PostService

@pytest.mark.asyncio
async def test_post_operations(mock_db):
    post_service = PostService(mock_db)
    
    # Test post creation
    post = await post_service.create_post(
        community_id="comm123",
        author_id="user123",
        title="Test Post",
        content="Test Content"
    )
    assert post["title"] == "Test Post"
    assert post["author_id"] == "user123"
    
    # Test adding comment
    success = await post_service.add_comment(
        post_id=post["id"],
        author_id="user456",
        content="Test Comment"
    )
    assert success is True
    
    # Test getting community posts
    posts = await post_service.get_community_posts("comm123")
    assert len(posts) == 1
    assert posts[0]["title"] == "Test Post"
