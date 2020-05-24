import asyncio
from aiohttp import request
from aiomultiprocess import Pool

async def get(url):
    async with request("GET", url) as response:
        return await response.text("utf-8")

async def main():
    urls = ["https://www.beautifulcode.co/", 'https://github.com/pbpranavk']
    async with Pool() as pool:
        result = await pool.map(get, urls)
        for response in result:
            print(f'response : {response} \n\n\n\n\n',)

if __name__ == "__main__":
    asyncio.run(main())