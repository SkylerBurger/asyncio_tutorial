import aiohttp
from aiohttp import ClientSession
import requests

import asyncio
import time


async def async_request(url, session):
    # print(f'Asynchronous HTTP request for {url} started.')
    reponse = await session.request(method='GET', url=url)
    # print(f'Asynchronous HTTP request for {url} completed.')

async def async_main():
    async with ClientSession() as session:
        tasks = []
        urls = [
            'https://pypi.org/rss/updates.xml',
            'https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc',
            'https://api.github.com/search/repositories?q=language:python&sort=updated&order=desc',
        ]

        for url in urls:
            tasks.append(async_request(url, session))
            
        await asyncio.gather(*tasks)

def sync_request(url):
    # print(f'Synchronous HTTP request for {url} started.')
    requests.get(url)
    # print(f'Synchronous HTTP request for {url} completed.')

def sync_main():
    sync_request('https://pypi.org/rss/updates.xml')
    sync_request('https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc')
    sync_request('https://api.github.com/search/repositories?q=language:python&sort=updated&order=desc')


def async_vs_sync_requests():
    # print('Synchronous HTTP requests:')
    s = time.perf_counter()
    sync_main()
    sync_elapsed = time.perf_counter() - s
    print(f'Synchronous HTTP requests executed in {sync_elapsed:0.2f} seconds.')

    # print('Asynchronous HTTP requests:')
    s = time.perf_counter()
    asyncio.run(async_main())
    async_elapsed = time.perf_counter() - s
    print(f'Asynchronous coroutines executed in {async_elapsed:0.2f} seconds.')


async_vs_sync_requests()