import sockets
import threading

bind_ip = "0.0.0.0"
bind_port = 5785

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))

server.listen(1)

print("[*] Listening for incoming connections {}:{}".format(bind_ip,bind_port))

def handle_clinet(client_socket):
	command = client_socket.recv(1024)
	client_socket.send("ACK")

While True:
	client,addr = server.accept()
	print("[*] Connection from {}:{}".format(addr[0],addr[1]))

	client.handler(target=handle_client,args=client,)

	client.handler.start()
	

