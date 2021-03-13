import socket, threading


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('0.0.0.0', 2222))

s.listen(10)



def server(c, a):
    
	while True:
        
		d = c.recv(1024)
        
		if d == 'close' or not d: break
        
		c.send(d)
    
	c.close()


		
while True:
    
	c, a = s.accept()
    
	t = threading.Thread(target=server, args=(c, a))
    
	t.start()
