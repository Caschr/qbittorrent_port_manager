# Start of the project

from time import sleep
from datetime import datetime, timedelta
from typing import Union
import os



# from dotenv import load_dotenv
# load_dotenv()

from login_manager import LoginManager

conn_info = {"host": os.getenv("HOST"),
             "port": os.getenv("PORT"),
             "username": os.getenv("USERNAME"),
             "password": os.getenv("PASSWORD"),
             }

def get_listening_port() -> Union[int, None]:
    port = None
    try:
        with LoginManager(conn=conn_info) as lm:
            app_preferences = lm.app_preferences()
            port = app_preferences['listen_port']
    
    except:
        print('QBittorrent Port Manager: Unable to find current port')
    
    return port

    

def set_new_port(port: int) -> bool:
    success = False
    try:
        with LoginManager(conn=conn_info) as lm:
            lm.app_set_preferences({"listen_port": port})
            print(f'QBittorrent Port Manager: Port changed to {str(port)}')
            success = True
        success = True
    except:
        print('QBittorrent Port Manager: Unable to set port in QBittorent')

    return success
        

def main():
    current_port = get_listening_port()
    current_port_timestamp = datetime.now()
    while True:
        forward_port = None
        try:
            with open('/gluetun/forwarded_port') as fp:
                forward_port = int(fp.readlines()[0])
        except (ValueError, IndexError, FileNotFoundError) as e:
            print('QBittorrent Port Manager: Unable to find forward port')
            print(e)

    
        if forward_port and current_port_timestamp + timedelta(hours=int(os.getenv('QBIT_PORT_FETCH_HOURS'))) < datetime.now():
           current_port_temp = get_listening_port()
           if current_port_temp:
               current_port = current_port_temp
               current_port_timestamp = datetime.now()
            
        if current_port and forward_port:
            if current_port != forward_port:
                set_new_port(port=forward_port)
        

        sleep(round(float(os.getenv('PORT_CHECK_FREQUENCY_MINUTES'))*60, 0))

if __name__ == '__main__':
    main()