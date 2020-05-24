async def run_loop(args):
	#Write async code here

def bootstrap(args):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run_loop(args))

def main():
    # create your args here
    # args = f(x)
    p =multiprocessing.Process(
        target=bootstrap,
        args=(args,)
        )
    p.start()