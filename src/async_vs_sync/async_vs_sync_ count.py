import asyncio
import time  # For demo purposes


async def async_count():
    print("ASYNC - One")
    await asyncio.sleep(1)
    print("ASYNC - Two")

async def async_main():
    await asyncio.gather(async_count(), async_count(), async_count())

def sync_count():
    print("SYNC - One")
    time.sleep(1)
    print("SYNC - Two")

def sync_main():
    for _ in range(3):
        sync_count()


def async_vs_sync_count():    
    print('Synchronous function calls:')
    s = time.perf_counter()
    sync_main()
    sync_elapsed = time.perf_counter() - s
    print(f"Synchronous function calls executed in {sync_elapsed:0.2f} seconds.")

    print('\nAsynchronous coroutines:')
    s = time.perf_counter()
    asyncio.run(async_main())
    async_elapsed = time.perf_counter() - s
    print(f"Asynchronous coroutines executed in {async_elapsed:0.2f} seconds.\n")


async_vs_sync_count()