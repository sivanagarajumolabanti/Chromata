import asyncio


async def num(number):
    print("before calling coroutine")
    await asyncio.sleep(1)
    print('after calling coroutine')
    return str(number)

loop = asyncio.get_event_loop()
# n = num(5)
l= loop.run_until_complete(num(5))
print(l)

loop = asyncio.get_event_loop()
# c = loop.create_task(num(5))
# u = loop.run_until_complete(c)
# print(u)

