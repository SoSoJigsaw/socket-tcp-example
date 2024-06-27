import socket
from encryption import load_keys, decrypt_message


def start_server():
    public_key, private_key = load_keys()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)

    print("Servidor aguardando conexão...")
    client_socket, addr = server_socket.accept()
    print(f"Conectado a {addr}")

    while True:
        encrypted_message = client_socket.recv(4096)
        if not encrypted_message:
            break
        decrypted_message = decrypt_message(encrypted_message, private_key)
        print(f"Mensagem recebida: {decrypted_message}")

    client_socket.close()
    server_socket.close()


if __name__ == '__main__':
    start_server()
