import socket
import sys
import threading

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('25.50.82.121', 10000)
print(sys.stderr, 'starting up on %s port %s' % server_address)
sock.bind(server_address)
sock.listen(5)

clients = {}
lock = threading.Lock()

def handle_client(client_socket, client_address):
    while True:
        try:
            data = client_socket.recv(999)
            if data:
                if data.decode()=="ping":
                    print()
                else:
                # Broadcast the received data to all connected clients except the sender
                    with lock:
                        for client in clients:
                            if client != client_socket:
                                client.send(data)
            else:
                # No data received, client has disconnected
                with lock:
                    del clients[client_socket]
                    client_socket.close()
                    print("Client disconnected:", client_address)
                    break
        except:
            with lock:
                del clients[client_socket]
                client_socket.close()
                print("Client disconnected:", client_address)
                break

while True:
    # Find connections
    connection, client_address = sock.accept()
    with lock:
        clients[connection] = client_address
        print("New client connected:", client_address)

    # Create a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(connection, client_address))
    client_thread.start()
