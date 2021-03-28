import socket




def display_map(game_map):
	print(game_map)


#host = input("ENTER SERVER IP (format 123.456.789.123)\n")
host = "localhost"
port = 39039

main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_socket.connect((host, port))
print("Connected to {} using port {}".format(host,port))


main_socket.send("Connected.".encode())


msg_in = main_socket.recv(1024)

print(msg_in.decode())


message = b""
while not (message == b"ddos" or message == b"stop" or message == b"disconnect"):

	message = input("> ")


	if(message == ''):
		message = "None"

	message = message.encode()

	main_socket.send(message)





	size_msg_in = eval(main_socket.recv(1024).decode('utf-8'))
	#print("Size {}".format(size_msg_in))
	main_socket.send(b'Ack')

	msg_in = ""

	for i in range(size_msg_in+1):
		msg_in = msg_in + main_socket.recv(1024).decode('utf-8')
		main_socket.send(b'Ack')





	if(message == "getBoard"):
		board = eval(msg_in)
		print(board)
	else:
		print(msg_in)

print("[INFO] Closing connection")
main_socket.close()
