import socket
import time
import pickle
import select
import errno
import sys

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234

def tryGetMessage(client_socket):
	time.sleep(0.1)
	try: 
		while True:
			#receive things
			message_header = client_socket.recv(HEADER_LENGTH)
			if not len(message_header):
				print("Connection closed by the server")
				sys.exit()
			message_length = int(message_header.decode('utf-8'))
			message = client_socket.recv(message_length).decode('utf-8')

			print(message)
		return True

	except IOError as e:
		if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
			print('Reading error', str(e))
			sys.exit()
		return False

	except Exception as e:
		print('General error', str(e))
		sys.exit()
		return False
	return False

my_username = input("Username: ")


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)

username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)

while True:
	message = input(f"{my_username} > ")

	if message:
		message = message.encode('utf-8')											#encode the message
		message_header = f"{len(message) :< {HEADER_LENGTH}}".encode('utf-8')		#encode the message header
		client_socket.send(message_header + message)								#send the message
	tryGetMessage(client_socket)
	



