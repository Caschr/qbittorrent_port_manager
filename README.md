# qBittorrent Port Manager
Automatically updates the listening port for the gluetun (or something else) on qBittorrent.

## Setup
First make sure you can connect to qBittorrent and that the portforwarding works (notice the green globe in lower right corner).
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
      - QBIT_PORT_FETCH_HOURS=24 # How often will program query qbit for its current port
      - PORT_CHECK_FREQUENCY_MINUTES=10 # How often will program check for new port
    volumes:
      - /gluetun:/gluetun
```


Note you need to provide the path to the gluetun directory where the file ```forwarded_port``` is located. 

