import socket
import datetime
import random

MAX_PACKET = 1024
time = datetime.datetime.now()
SERVER_NAME = "Gilad's Server"
QUEUE_LEN = 1


while True:
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        my_socket.bind(('0.0.0.0', 1729))
        my_socket.listen(QUEUE_LEN)
        client_socket, client_address = my_socket.accept()
        try :
            request = client_socket.recv(MAX_PACKET).decode()
            print('server received: ' + request)
        except socket.error as err:
            print('received socket error on client socket' + str(err))
        finally:
            mode = client_socket.recv(MAX_PACKET).decode()
            if(mode == "TIME"):
                client_socket.send(f"The current date and time is: {time}".encode())
            elif(mode == "NAME"):
                client_socket.send(('The name of the server is: ' + SERVER_NAME).encode())
            elif(mode == "RAND"):
                client_socket.send(('The Random Number Is: ' + str(random.randint(1,10))).encode())
            else:
                print("Invalid argument; the client didnt choose any of the options")
            client_socket.close()
    except socket.error as err:
        print('received socket error on server socket' + str(err))
    finally:
        my_socket.close()
