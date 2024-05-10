# Start of the project

from time import sleep
import qbittorrentapi
import os



# from dotenv import load_dotenv
# load_dotenv()

conn_info = {"host": os.getenv("HOST"),
             "port": os.getenv("PORT"),
             "username": os.getenv("USERNAME"),
             "password": os.getenv("PASSWORD"),
             }


def main():
    while True:
        current_port = None
        forward_port = None
        try:
            with open('/gluetun/forward_port') as fp:
                forward_port = int(fp.readlines()[0])
        except (ValueError, IndexError, FileNotFoundError) as e:
            print('Unable to find forward port')
            print(e)

    
        if forward_port:
            client = qbittorrentapi.Client(**conn_info)
            try:
                client.auth_log_in()
            except qbittorrentapi.LoginFailed as e:
                print('Unable to connect to QBittorrent')
                print(e)
        
        
            try:
                app_preferences = client.app_preferences()
                current_port = app_preferences['listen_port']
            
            except:
                print('Unable to find current port')
                current_port = None
            
        if current_port and forward_port:
            if current_port != forward_port:
                try:
                    client.app_set_preferences({"listen_port": forward_port})
                    print(f'QBittorent port updater: Port changed to {str(forward_port)}')
                except:
                    print('Unable to set port in QBittorent')
        

        try:
            client.auth_log_out()
        except:
            pass

        sleep(300) # 300 minutes

if __name__ == '__main__':
    main()