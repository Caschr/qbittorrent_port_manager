# Start of the project

from datetime import time
import qbittorrentapi
from dotenv import load_dotenv
import os


load_dotenv()
conn_info = {"host": os.getenv("host"),
             "port": os.getenv("port"),
             "username": os.getenv("username"),
             "password": os.getenv("password"),
             }



while True:
    try:
        with open('/home/casper/forward_port') as fp:
            forward_port = int(fp.readlines()[0])
    except (ValueError, IndexError):
        forward_port = None
    
    client = qbittorrentapi.Client(**conn_info)

    try:
        client.auth_log_in()
    except qbittorrentapi.LoginFailed as e:
        print(e)
    
    if forward_port:
        try:
            app_preferences = client.app_preferences()
            current_port = app_preferences['listen_port']
        
        except:
            current_port = None
        
    if current_port and forward_port:
        if current_port != forward_port:
            try:
                client.app_set_preferences({"listen_port": forward_port})
            except:
                pass
    


    client.auth_log_out()

    time.sleep(30)