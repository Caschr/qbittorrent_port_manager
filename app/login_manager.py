
from typing import Union
from qbittorrentapi import Client, LoginFailed

class LoginManager:

    def __init__(self, conn: dict) -> None:
        self.conn = conn
    
    def __enter__(self) -> Union[Client, None]:
        try:
            self.client = Client(**self.conn)
            self.client.auth_log_in()
            return self.client
        
        except LoginFailed as e:
            print('QBittorrent Port Manager: Unable to connect to QBittorrent')
            print(e)
            return None     

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            self.client.auth_log_out()
        
        except:
            pass
    



