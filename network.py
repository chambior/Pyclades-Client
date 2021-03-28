import socket

#host = input("ENTER SERVER IP (format 123.456.789.123)\n")
host = "localhost"
port = 39039

main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_socket.connect((host, port))
print("Connecté à {} sur le port {}".format(host,port))


main_socket.send("Connecté.".encode())


msg_in = main_socket.recv(1024)

print(msg_in.decode())


def send(message):
	if(message == ''):
		message = "None"

	message = message.encode()

	main_socket.send(message)


	size_msg_in = eval(main_socket.recv(256).decode())
	#print("Size {}".format(size_msg_in))
	main_socket.send(b'Ack')

	msg_in = ""

	for i in range(size_msg_in+1):
		msg_in = msg_in + main_socket.recv(256).decode()
		main_socket.send(b'Ack')

	if(message == "getBoard"):
		board = eval(msg_in)

	return msg_in
