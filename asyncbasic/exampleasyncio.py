import asyncio
import logging

logger = logging.getLogger('example')


async def simple_interest(p,t,r):
    await asyncio.sleep(1)
    return (p*t*r)/100


async def main():
    # loop = asyncio.get_event_loop()
    # loop.set_debug(True)
    # s = asyncio.gather(simple_interest(10,10,10), simple_interest(20,20,20))
    # s1 = simple_interest(10,10,10)
    # s2 = simple_interest(20,20,20)
    # l1 = loop.run_until_complete(s1)
    # l2 = loop.run_until_complete(s2)
    # print(l1)
    # print(l2)
    s = loop.create_task(simple_interest(5,5,5))
    s1 = loop.create_task(simple_interest(10,10,10))
    await asyncio.wait([s,s1])
    return s, s1

    # print(l)


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s %(levelname)-5s %(threadName)-10s %(name)-15s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.DEBUG
    )
    logging.getLogger("asyncio").setLevel(logging.CRITICAL)
    loop = asyncio.get_event_loop()
    loop.set_debug(True)
    d,d1= loop.run_until_complete(main())
    print(d1.result())

# foo = {1:'10',2:'20',3:'30',4:'40'}
# del foo[1]
# foo[1]='10'
# del foo[4]
# print(len(foo))
# print(foo)