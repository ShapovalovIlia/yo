import redis.asyncio as aioredis # type: ignore


async def get_redis_async_conn():
    return await aioredis.from_url(
        f"redis://127.0.0.1:6379", encoding="utf-8", decode_responses=True
    )  # TODO: сделать логику через диренв
