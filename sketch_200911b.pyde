import socket
main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connected = False


class button:
    def __init__(self,label,size,coords):
        self.label = label
        self.size = size
        self.coords = coords
    def display(self):
        if not self.isClicked():
            fill(255)
            noStroke()
            rect(self.coords[0]+1, self.coords[1]+1, self.size[0]-1, self.size[1]-1)
            
            stroke(150)
            line(self.coords[0], self.coords[1], self.coords[0] + self.size[0], self.coords[1])
            line(self.coords[0], self.coords[1], self.coords[0], self.coords[1] + self.size[1])
            stroke(100)
            line(self.coords[0], self.coords[1] + self.size[1], self.coords[0] + self.size[0], self.coords[1] + self.size[1])
            line(self.coords[0] + self.size[0], self.coords[1], self.coords[0] + self.size[0], self.coords[1] + self.size[1])
        else:
            self.displayClicked()
        
    def displayClicked(self):
        fill(255)
        noStroke()
        rect(self.coords[0]+1, self.coords[1]+1, self.size[0]-1, self.size[1]-1)
        stroke(100)
        line(self.coords[0], self.coords[1], self.coords[0] + self.size[0], self.coords[1])
        line(self.coords[0], self.coords[1], self.coords[0], self.coords[1] + self.size[1])
        stroke(150)
        line(self.coords[0], self.coords[1] + self.size[1], self.coords[0] + self.size[0], self.coords[1] + self.size[1])
        line(self.coords[0] + self.size[0], self.coords[1], self.coords[0] + self.size[0], self.coords[1] + self.size[1])
        
        
        
    def isClicked(self):
        if mouseX > self.coords[0] and mouseY > self.coords[1] and mouseX < self.coords[0] + self.size[0] and mouseY < self.coords[1] + self.size[1] and mousePressed:
            clicked = True
        else:
            clicked = False
        return clicked

class textBox:
    def __init__(self,label,coords):
        self.label = label
        self.coords = coords
    def display(self):
        fill(0)
        text(self.label, self.coords[0], self.coords[1])

class commandLine:
    
    def __init__(self, coords, size):
        self.coords = coords
        self.size = size
        self.text = ""
        
    def display(self):
        stroke(0)
        fill(75)
        rect(self.coords[0], self.coords[1], self.size[0], self.size[1])
        fill(255)
        text("> " + self.text, self.coords[0], self.coords[1] + self.size[1])





class console:
    def __init__(self, coords, size, lines):
        self.coords = coords
        self.size = size
        self.lines = lines
        self.cursor = 0
        self.slider = 0
        self.sliderPressed = False
        
        self.sliderXmax = 0
        self.sliderXmin = 0
        self.sliderYmax = 0
        self.sliderYmin = 0
        
    def moveSlider(self):
        if mouseX <= self.sliderXmax and mouseX >= self.sliderXmin and mouseY <= self.sliderYmax and mouseY >= self.sliderYmin and mousePressed:
            self.sliderPressed = True
        elif not mousePressed:
            self.sliderPressed = False
            
    
        if self.sliderPressed:
            
            nbpositions = len(self.lines) - 49
            
            
            ys = (float(self.size[1] - 15) / float(nbpositions))
            dec = 0
            if ys < 15:
                dec = -7
            
            self.slider = int((self.coords[1] + self.size[1] - mouseY + dec ) / ys)
            if self.slider >= nbpositions-1:
                self.slider = nbpositions-1
            if self.slider < 0:
                self.slider = 0
            
        
        
    def displaySlider(self):
        
        if len(self.lines) > 50:
        
            
            
            
            stroke(100)
            fill(200)
            rect(self.coords[0] + self.size[0], self.coords[1], -10, self.size[1])
            
            stroke(170)
            fill(255)
            
            
            nbpositions = len(self.lines) - 49
            
            ys = int( float(self.size[1] - 15) / float(nbpositions))
            if ys < 15:
                ys = 15
                
            ys = - ys
            
            xo = self.coords[0] + self.size[0] -10
            yo =  self.coords[1] + self.size[0] - self.slider * (float(self.size[0] - 15)) / float((nbpositions))
            
            yo = int(yo)
            
            xs = 10
            
            
            if self.slider == nbpositions-1:
                ys = self.coords[1] - yo
            
            self.sliderXmax = xo + xs
            self.sliderYmax = yo
            self.sliderXmin = xo
            self.sliderYmin = yo + ys
            
            rect(xo,yo,xs,ys)
            
    def displayLines(self):
        yOffset = 0
        fill(200)
        for line in self.lines[self.slider:self.slider+50]:
            text(line, self.coords[0], self.coords[1] + self.size[1] - yOffset)
            yOffset += 10
            
    
    def display(self):
        stroke(0)
        fill(50)
        rect(self.coords[0], self.coords[1], self.size[0], self.size[1])
        
        self.displaySlider()
        self.displayLines()
        
        
def displayBoard(board):
    xOffset = 550
    yOffset = 300
    #print("Début displayboard")
    for i in board['tiles']:
        ei = i
        #print("{} - {},{}".format(i, xOffset + eval(ei)[0] * 20 + eval(ei)[1] * 20, yOffset + eval(ei)[0] * 35 - eval(ei)[1] * 35))
        
        ellipse(xOffset + eval(ei)[0] * 20 + eval(ei)[1] * 20, yOffset + eval(ei)[0] * 35 - eval(ei)[1] * 35,40,40)

        

def setup():
    size(1080,720)
    background(200,240,255)
    noStroke()


def draw():
    background(200,240,255)
    global connected
    global mcoords
    global cnsl
    global cmd
    global oldkeys
    global board
    if not connected:
        #if 
        
        
        
        
        
        
        try:
            host = "localhost"#input("ENTER SERVER IP (format 123.456.789.123)\n")
            port = 39039
        
            
            main_socket.connect((host, port))
            
        
        
            main_socket.send("Connected.".encode())
        
        
            
            msg_in = main_socket.recv(1024)
            
            lines = [msg_in[-47:],msg_in[:33],msg_in[34:-47], "Connection a {} sur le port {}".format(host,port)]
            
            connected = True
            
            cnsl = console([10,35],[500,500], lines)
            mcoords = textBox(str(mouseX) + " - " + str(mouseY), [900,650])
            cmd = commandLine([10,537],[500,10])
            
            oldkeys = []
            board = {'tiles': {}}
        except:
            fill(0)
            text("Connexion en cours...",512,256)
            print("Echec de la connexion a {}. Nouvelle tentative".format(host))
            
            
        
    else:
        
        try:
            
        
            b_send = button("Valider", [80, 20], [10, 10])
            
            mcoords.display()
            mcoords.label = str(mouseX) + " - " + str(mouseY)
            
            cnsl.display()
            cnsl.moveSlider()
            b_send.display()
            
            cmd.display()
            
            
            
            
            keyIsntAlreadyPressed = True
            for oldkey in oldkeys:
                if oldkey == key:
                    keyIsntAlreadyPressed = False
            
            
            if keyPressed and keyIsntAlreadyPressed:
                if key != "\n" and key != 65535 and key != BACKSPACE:
                    cmd.text = cmd.text + key
                elif key == BACKSPACE:
                    cmd.text = cmd.text[:-1]
                elif key == "\n":
                    
                    message = cmd.text
                    cmd.text = ""
                    cnsl.lines.insert(0,"> " + message)
                    
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
                        
                        
                        
                        
                    else:
                        cnsl.lines.insert(0,msg_in)
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                oldkeys.append(key)
                
            if not keyPressed:
                oldkeys = []
            
            displayBoard(board)
        except OSError:
            connected = 0
