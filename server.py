import socket
import threading

HOST = '192.168.1.12'   # Localhost (better than 0.0.0.0 for local testing)
PORT = 8003

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:
            remove_client(client)

def remove_client(client):
    if client in clients:
        index = clients.index(client)
        clients.remove(client)
        client.close()
        nickname = nicknames[index]
        nicknames.remove(nickname)
        broadcast(f"Server: {nickname} left the chat.".encode('utf-8'))

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            if not message:
                break
            broadcast(message)
        except:
            break
    remove_client(client)

def receive_connections():
    print(f"Server running on {HOST}:{PORT} ...")
    
    while True:
        client, address = server.accept()
        print(f"Connected with {address}")

        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        client.send("Server: Connected to the chat room.".encode('utf-8'))
        broadcast(f"Server: {nickname} joined the chat.".encode('utf-8'))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

# 🔴 START SERVER HERE
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()        # ⭐ VERY IMPORTANT ⭐
receive_connections()  # ⭐ CALL FUNCTION ⭐