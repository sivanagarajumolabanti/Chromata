import asyncio


async def a_hello(name):
    return 'hi '+name


def hello(name):
    return 'hi '+name

# def run_hello(coroutine):
#     try:
#         coroutine.send(None)
#     except StopIteration as s:
#         return s.value
#
# h = hello('siva')
# print(h)
# # ah = a_hello('raj')
# # print(ah)
#
# rh = run_hello(a_hello('siva'))
# print(rh)

loop = asyncio.get_event_loop()
ah= a_hello('siva')
p = loop.run_until_complete(ah)
print(p)