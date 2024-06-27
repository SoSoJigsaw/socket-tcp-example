import socket
from encryption import load_keys, encrypt_message


def start_client():
    public_key, _ = load_keys()

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    while True:
        message = input("Digite a mensagem: ")
        if message.lower() == 'sair':
            break
        encrypted_message = encrypt_message(message, public_key)
        client_socket.sendall(encrypted_message)

    client_socket.close()


if __name__ == '__main__':
    start_client()
