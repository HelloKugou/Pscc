from test.test_1 import a
import asyncio
loop  = asyncio.get_event_loop()
print(a)
loop.run_until_complete(a())