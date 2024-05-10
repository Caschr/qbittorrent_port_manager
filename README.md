# QBittorent Port Manager
Automatically updates the listening port for the gluetun (or something else) on Qbittorent.

## Setup
First make sure you can connect to QBittorent and that the portforwarding works (notice the green globe in lower right corner).
Then use the following docker-compose.yml file

```
  qbittorrent_port_manager:
    image: thecc90/qbittorrent_port_manager:latest
    restart: unless-stopped
    network_mode: "service: gluetun"
    environment:
      - HOST=192.168.1.1 # CHANGE TO YOUR HOST IP
      - PORT=8080 # CHANGE_TO YOUR PORT
      - USERNAME=username # CHANGE TO YOUR USERNAME
      - PASSWORD=password # CHANGE TO YOUR PASSWORD
    volumes:
      - /gluetun:/gluetun
```


Note you need to provide the path to the gluetun directory where the file ```forwarded_port``` is located. 

