import asyncio


async def sleep(name, delay, repeat):
    for i in range(1, repeat+1):
        await asyncio.sleep(delay)
    return name

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    s = asyncio.gather(sleep('siva', 3, 1), sleep('naga', 5, 1), sleep('raju', 7 ,1))
    # s = sleep('siva', 3, 1)
    l = loop.run_until_complete(s)
    print(l)
