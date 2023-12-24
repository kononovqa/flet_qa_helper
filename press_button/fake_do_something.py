import asyncio


async def do_something():
    await asyncio.sleep(0.1)


async def do_something_failed():
    await asyncio.sleep(0.1)
    assert 0
