import rsa


def generate_keys():
    # Gera chaves pública e privada
    public_key, private_key = rsa.newkeys(2048)
    with open('public_key.pem', 'wb') as pub_file:
        pub_file.write(public_key.save_pkcs1('PEM'))
    with open('private_key.pem', 'wb') as priv_file:
        priv_file.write(private_key.save_pkcs1('PEM'))
    print("Chaves geradas e salvas em 'public_key.pem' e 'private_key.pem'.")


if __name__ == '__main__':
    generate_keys()
