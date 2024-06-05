"""Testing when a UUID is not provided."""
import pytest
import os
from mcci_api import APIClient, NoUsernameOrUUIDException

@pytest.mark.asyncio
async def test_uuid():
    """Testing when a UUID is not provided."""
    api_key = os.getenv("MCCI_API_KEY")
    contact_email = os.getenv("CONTACT_EMAIL")
    user_agent = f"osfanbuff63/mcci-api-python via actions/runner, {contact_email}"
    client = APIClient(api_key, user_agent)
    with pytest.raises(NoUsernameOrUUIDException):
        await client.get_player()