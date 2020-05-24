import asyncio

# This dosen't work :(

# Producer code
async def validate_and_raise():
    if( 2 == 2):
        await raise_alert()

# Consumer code
async def raise_alert():
    print("About to send a mail")
    await asyncio.sleep(1)
    print("We have sent an email")

# Buisness logic
async def some_business_logic():
    task1 = asyncio.create_task(print("1"))
    task2 = asyncio.create_task(await validate_and_raise())
    task3 = asyncio.create_task(print("2"))

    await task1
    await task2
    await task3

# Invokation of business logic in serve.py
asyncio.run(some_business_logic())


# Neither dose this :(

# Producer code
# async def validate_and_raise():
#     if( 2 == 2):
#         await raise_alert()

# # Consumer code
# async def raise_alert():
#     print("About to send a mail")
#     await asyncio.sleep(1)
#     print("We have sent an email")

# # Buisness logic
# async def some_business_logic():
#     print("1")
#     task2 = asyncio.create_task(await validate_and_raise())
#     print("2")
#     await task2

# # # Invokation of business logic in serve.py
# asyncio.run(some_business_logic())