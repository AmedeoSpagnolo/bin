### Sources
[https://null-byte.wonderhowto.com/how-to/set-up-headless-raspberry-pi-hacking-platform-running-kali-linux-0176182/](https://null-byte.wonderhowto.com/how-to/set-up-headless-raspberry-pi-hacking-platform-running-kali-linux-0176182/)

### Ingredients


### Description 

- Download Kali Linux Image for the Raspberry Pi [https://www.kali.org/downloads/](https://www.kali.org/downloads/)
- Flash the Image to the Micro SD Card [https://etcher.io/](https://etcher.io/)
- Boot into Kali Linux
```
root@toor
```
- Expand your installation to the size of the partition

```
resize2fs /dev/mmcblk0p2
```
- Update

```
apt-get update
apt-get upgrade
apt-get dist-upgrade
```
- Change password

```
passwd root
```
- Enable SSH

```
apt-get install openssh-server
update-rc.d -f ssh remove
update-rc.d -f ssh defaults

cd /etc/ssh/
mkdir insecure_old
mv ssh_host* insecure_old
dpkg-reconfigure openssh-server

sudo service ssh restart
update-rc.d -f ssh enable 2 3 4 5

sudo service ssh status
```

- SSH remote login

```
ssh root@(your IP address)
```

- set up network interfaces

```
# /etc/network/interfaces

auto lo
iface lo inet loopback

auto eth0
iface eth0 inet dhcp

allow-hotplug wlan0
iface wlan0 inet manual
  wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf

iface default inet dhcp

# /etc/wpa_supplicant/wpa_supplicant.conf

ctr_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
  scan_ssid=1
  priority=5
  ssid=""
  psk=""
}

## generate with: wpa_passphrase SSID

```
