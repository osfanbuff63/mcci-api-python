"""A basic example that gets the amount of coins and prints it."""

import os
import asyncio
from mcci_api import APIClient

async def _main():
    # Read the API key from the environment variable `MCCI_API_KEY`
    api_key = os.getenv("MCCI_API_KEY")
    client = APIClient(api_key, "<insert_user_agent>")
    result = await client.get_player("2ef24d23-d958-49c4-b6db-a0f4e94d592d") # osfanbuff63
    print(f"{result.collections.currency.coins} Coins")

asyncio.run(_main())