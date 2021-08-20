import json
import time as time_true
import pathlib
import pandas as pd
from td.client import TDClient
from td.utils import TDUtilities

class PyRobot():

    def __init__(self, client_id: str, redirect_uri: str, paper_trading: bool = True, credentials_path: str = None, trading_account: str = None) -> None:

        # Set the attirbutes
        self.trading_account = trading_account
        self.client_id = client_id
        self.redirect_uri = redirect_uri
        self.credentials_path = credentials_path
        self.session: TDClient = self._create_session()
        self.trades = {}
        self.historical_prices = {}
        self.stock_frame: StockFrame = None
        self.paper_trading = paper_trading

        self._bar_size = None
        self._bar_type = None

    def _create_session(self) -> TDClient:
        
        # Create a new instance of the client
        td_client = TDClient(
            client_id=self.client_id,
            redirect_uri=self.redirect_uri,
            credentials_path=self.credentials_path
        )

        # log the client into the new session
        td_client.login()

        return td_client