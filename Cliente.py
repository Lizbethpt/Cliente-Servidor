import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'  
    port = 12345        

    client_socket.connect((host, port))
    print(f"Conectado al servidor {host}:{port}")

    while True:
        mensaje = input("Cliente: ")
        client_socket.send(mensaje.encode())  
        if mensaje.lower() == 'salir':
            print("Cerrando conexión...")
            break
        respuesta = client_socket.recv(1024).decode()  
        print(f"Servidor: {respuesta}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
