import asyncio


async def do_something():
    await asyncio.sleep(0.5)


async def do_something_failed():
    await asyncio.sleep(0.5)
    assert 0
