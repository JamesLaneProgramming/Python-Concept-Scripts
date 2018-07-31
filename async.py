import asyncio

async def countdown(n):
    while n > 0:
        print(str(n) + " Seconds left in the async wait")
        n -= 1
        print("This is running before the wait operation on the seperate thread")
        await asyncio.sleep(1)

async def main():
    #This variable contains all of the required callbacks for the program to continue.
    futures = asyncio.gather(
        countdown(3)
    )
    print("Before Loop Altogether")
    await futures
    print("After the loop")
    loop.stop()

loop = asyncio.get_event_loop()
asyncio.ensure_future(main())
loop.run_forever()
