import rsa


def load_keys():
    with open('public_key.pem', 'rb') as pub_file:
        public_key = rsa.PublicKey.load_pkcs1(pub_file.read())
    with open('private_key.pem', 'rb') as priv_file:
        private_key = rsa.PrivateKey.load_pkcs1(priv_file.read())
    return public_key, private_key


def encrypt_message(message, public_key):
    return rsa.encrypt(message.encode(), public_key)


def decrypt_message(encrypted_message, private_key):
    return rsa.decrypt(encrypted_message, private_key).decode()


if __name__ == '__main__':
    public_key, private_key = load_keys()
    message = "Teste de mensagem"
    encrypted_message = encrypt_message(message, public_key)
    print(f"Mensagem criptografada: {encrypted_message}")
    decrypted_message = decrypt_message(encrypted_message, private_key)
    print(f"Mensagem descriptografada: {decrypted_message}")
