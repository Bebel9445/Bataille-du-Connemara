import socket
import sys
import threading
import time

def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if data:
                print(data.decode())
            else:
                # No data received, server has disconnected
                client_socket.close()
                break
        except:
            client_socket.close()
            break


def ping(socket):
    while True :
        time.sleep(1)
        ping="ping"
        socket.send(ping.encode())




# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('25.50.82.121', 10000)
print(sys.stderr, 'connecting to %s port %s' % server_address)

try:
    sock.connect(server_address)

    # Start a separate thread to receive messages from the server
    receive_thread = threading.Thread(target=receive_messages, args=(sock,))
    receive_thread.start()
    ping_thread = threading.Thread(target=ping, args=(sock,))
    ping_thread.start()


    while True:
        message = input('Message: ')
        if message == 'quit':
            break
        sock.send(message.encode())

except ConnectionRefusedError:
    print("Server is not available.")
finally:
    sock.close()
