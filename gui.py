from appJar import gui
import socket

main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# handle button events
def press(button):
	if button == "Quitter":
		app.stop()
	elif button == "Connecter":
		host = "localhost"#input("ENTER SERVER IP (format 123.456.789.123)\n")
		port = 39039

		
		main_socket.connect((host, port))
		print("Connected to {} using port {}".format(host,port))


		main_socket.send("Connected.".encode())



		msg_in = main_socket.recv(1024)

		print(msg_in.decode())

		app.removeAllWidgets()
		app.addEntry("cmd")
		app.addButton("Valider",press)
		app.addLabel("last_cmd", "Connecté\nTapez 'help' pour savoir ce que vous pouvez faire")
		app.addButton("Quitter", press)
		app.show("Valider")
	else:
		cmd = app.getEntry("cmd")
		try:
			app.addLabel("last_cmd", cmd)
		except:
			app.setLabel("last_cmd", cmd)
		
		message = b""
		if not (message == b"ddos" or message == b"stop" or message == b"disconnect"):
			
			message = app.getEntry("cmd")
			

			if(message == ''):
				message = "None"
			
			message = message.encode()
			
			main_socket.send(message)





			size_msg_in = eval(main_socket.recv(1024).decode())
			#print("Size {}".format(size_msg_in))
			main_socket.send(b'Ack')

			msg_in = ""

			for i in range(size_msg_in+1):
				msg_in = msg_in + main_socket.recv(1024).decode()
				main_socket.send(b'Ack')



			

			if(message == "getBoard"):
				board = eval(msg_in)
				app.setLabel("last_cmd", board)
			else:
				app.setLabel("last_cmd", msg_in)


# add & configure widgets - widgets get a name, to help referencing them later




# create a GUI variable called app
app = gui("Pyclades GUI", "400x200")
app.addLabel("title", "Pyclades")

# link the buttons to the function called press
app.addButton("Connecter", press)
app.addButton("Quitter", press)


# start the GUI
app.go()