import asyncio

# # Producer code
# async def validate_and_raise():
#     if( 2 == 2):
#         await raise_alert()

# # Consumer code
# async def raise_alert():
#     print("About to send a mail")
#     await asyncio.sleep(1)
#     print("We have sent an email")

async def slow_function():
    print("From slow 1")
    await call_to_another_func()
    print("From slow 2")
    #return "slow_function"

async def call_to_another_func():
    print("begin from call_to_another_func")
    await asyncio.sleep(1)
    print("done from call_to_another_func")

async def fast_function():
    print("From fast 1")
    await asyncio.sleep(0.5)
    print("From fast 2")
    #return "fast function"
# Buisness logic
async def some_business_logic():
    print("1")
    print(2)
    task1 = asyncio.create_task(slow_function())
    print(3)
    task2 = asyncio.create_task(fast_function())
    await task1
    print(4)
    await task2
    #await validate_and_raise()
    print(5)


print("before")
# Invokation of business logic in serve.py
asyncio.run(some_business_logic())
print("after")
