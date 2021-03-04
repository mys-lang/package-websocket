import logging
import asyncio
import websockets

logging.basicConfig(level=logging.DEBUG)

async def hello(websocket, path):
    print("Connected!")

    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")


start_server = websockets.serve(hello, "localhost", 20000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
