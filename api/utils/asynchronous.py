# https://medium.com/hackernoon/how-to-run-asynchronous-web-requests-in-parallel-with-python-3-5-without-aiohttp-264dc0f8546
import asyncio
from concurrent.futures import ThreadPoolExecutor
import requests


def create_asynchronous(func, args):
    async def get_asynchronous():
        with ThreadPoolExecutor(max_workers=10) as executor:
            with requests.Session() as session:
                loop = asyncio.get_event_loop()
                tasks = [
                    loop.run_in_executor(
                        executor,
                        func,
                        *(arg, session)
                    )
                    for arg in args
                ]
                return await asyncio.gather(*tasks)
    return get_asynchronous


def map_asynchronous(func, args):
    asynchronous_func = create_asynchronous(func, args)
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(asynchronous_func())
    loop.run_until_complete(future)
    return future.result()
