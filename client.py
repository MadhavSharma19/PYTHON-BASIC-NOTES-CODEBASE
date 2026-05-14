import socket
import threading
import sys



# Define the server address and port
HOST = '192.168.1.1' # Use 'localhost' or the actual server IP address
PORT = 8003

# Get the user's desired nickname
nickname = input("Choose your nickname: ")
# Function to receive messages from the server
def receive(client_socket):
    while True:
        try:
            # Receive message from server and print it
            message = client_socket.recv(1024).decode('utf-8')
            # The first message is the 'Welcome' or 'Connected' message
            if 'Server: Connected to the chat room.' in message:
                print(message)
            else:
                # Regular chat messages
                print(message)
        except:
            # Handle disconnection
            print("Server disconnected or an error occurred.")
            client_socket.close()
            sys.exit() # Exit the client program

# Function to send messages to the server
def write(client_socket):
    while True:
        try:
            # Get user input
            message = input('')
            # Format the message to include the nickname
            full_message = f"{nickname}: {message}"
            # Send the encoded message to the server
            client_socket.send(full_message.encode('utf-8'))
        except:
            # Exit loop on error (e.g., if socket is closed)
            break

# Function to start the client
def start_client():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORT))

        # Send the nickname immediately after connecting
        client.send(nickname.encode('utf-8'))

        # Start receiving messages in a separate thread
        receive_thread = threading.Thread(target=receive, args=(client,))
        receive_thread.start()

        # Start sending messages in a separate thread
        write_thread = threading.Thread(target=write, args=(client,))
        write_thread.start()

    except ConnectionRefusedError:
        print(f"Connection refused. Make sure the server is running on {HOST}:{PORT}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
     start_client()