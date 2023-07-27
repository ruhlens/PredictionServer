import asyncio 
import websockets 
import pandas as pd 
from ArimaModel import ArimaModel
import json

class PredictionsServer:
    '''
    Class that holds a server which outputs predictions data based on an ARIMA model.
    '''

    def __init__(self, host, port):
        '''
        Constructor for the PredictionsServer class.
        '''
        self.host = host
        self.port = port
        self.server = None

    async def handleClient(self, websocket, path):
        '''
        Handles the server and is in charge of operations at each iteration of the server.
        '''
        # Handle the websocket connection here
        while True:
            model = ArimaModel().createPredictionsDF('AAPL')
            #data = model.to_json()
            #data = model.to_dict(orient='records')
            #json_data = json.dumps(data)
            data = model.to_dict(orient='index''dict') 
            parsedDict = {str(key): value['y_pred'] for key, value in data.items()}
            jsonData = json.dumps(parsedDict)
            await websocket.send(jsonData)
            await asyncio.sleep(1)

    async def start(self):
        '''
        Start the server and run the client handler.
        '''
        self.server = await websockets.serve(self.handleClient, self.host, self.port)
        print(f"WebSocket server started at ws://{self.host}:{self.port}")
        # Keep the server running indefinitely
        await self.server.wait_closed()

    def stop(self):
        '''
        Stop the server.
        '''
        if self.server:
            self.server.close()

    def run(self):
        '''
        Handles the server loop.
        '''
        asyncio.run(self.start())
