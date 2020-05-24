async def fetch(url):
    return await aiohttp.request("GET", url)

async def fetch_two(url_a, url_b):
    future_a = fetch(url_a)
    future_b = fetch(url_b)
    a, b = asyncio.gather(future_a, future_b)
    return a,b