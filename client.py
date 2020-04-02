# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 19:55:30 2020

@author: jiang
"""

import websockets
import asyncio


cs = set()


async def talk(websocket, path):

    while True:
        if (not websocket in cs):
            cs.add(websocket)
            msg = 'Welcome: ' + str(websocket.remote_address)
        else:
            msg = str(websocket.remote_address) + 'says: ' + str(await websocket.recv())
        await asyncio.wait([ws.send(msg) for ws in cs])



start_server = websockets.serve(talk, '172.20.10.4', 8764)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
