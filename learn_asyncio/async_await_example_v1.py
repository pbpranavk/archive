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
    await validate_and_raise()
    print("2")

# Invokation of business logic in serve.py
print ("before")
asyncio.run(some_business_logic())
print ("after")
