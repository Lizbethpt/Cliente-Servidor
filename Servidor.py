import socket

def start_server():
    # Crear un socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'  # Dirección IP del servidor (localhost)
    port = 12345        # Puerto para la conexión
    server_socket.bind((host, port))
    print(f"Servidor iniciado en {host}:{port}")

    # Escuchar conexiones entrantes
    server_socket.listen(1)
    print("Esperando conexiones...")

    # Aceptar una conexión
    client_socket, client_address = server_socket.accept()
    print(f"Conexión establecida con {client_address}")

    # Interacción con el cliente
    while True:
        data = client_socket.recv(1024).decode()  # Recibir datos
        if not data or data.lower() == 'salir':
            print("Cerrando conexión...")
            break
        print(f"Cliente: {data}")
        respuesta = input("Servidor: ")
        client_socket.send(respuesta.encode())  # Enviar respuest

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
