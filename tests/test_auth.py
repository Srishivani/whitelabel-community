import pytest
from whitelabel_community.auth import AuthService
from datetime import timedelta

@pytest.mark.asyncio
async def test_auth_flow():
    auth_service = AuthService()
    
    # Test token creation
    test_data = {"user_id": "123", "username": "testuser"}
    token = await auth_service.create_access_token(
        data=test_data,
        expires_delta=timedelta(minutes=5)  # Longer expiration for testing
    )
    assert token is not None
    
    # Test token verification
    payload = await auth_service.verify_token(token)
    assert payload["user_id"] == test_data["user_id"]
    assert payload["username"] == test_data["username"]
    assert "exp" in payload
