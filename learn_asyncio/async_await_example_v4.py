import asyncio

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
    print("1")
    task = asyncio.create_task(validate_and_raise())
    print("2")

    await task

# Invokation of business logic in serve.py
asyncio.run(some_business_logic())