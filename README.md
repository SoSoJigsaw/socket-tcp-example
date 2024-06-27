# Socket TCP Example App 

- Aplicativo de Troca de Mensagens com Criptografia Assimétrica

## Descrição

- Este projeto implementa um aplicativo de troca de mensagens TCP/IP com criptografia de ponta a ponta usando criptografia assimétrica. 

## Estrutura do Projeto

```lua
socket-tcp-example/
|-- client.py
|-- server.py
|-- key_gen.py
|-- encryption.py
|-- README.md
```

## Passo a Passo para Execução

### 1. Geração de Chaves

- Primeiro, gere as chaves pública e privada:

```sh
python key_gen.py
```
As chaves serão salvas nos arquivos `public_key.pem` e `private_key.pem`.

### 2. Execução do Servidor

- Abra um terminal e execute o servidor:

```sh
python server.py
```

### 3. Execução do Cliente

- Abra um novo terminal e execute o cliente:

```sh
python client.py
```

### 4. Envio de Mensagens

- No terminal do cliente, digite as mensagens que deseja enviar. Para sair, digite `sair`.

### 5. Recebimento de Mensagens

- No terminal do servidor, observe as mensagens descriptografadas chegando. O servidor exibirá cada mensagem recebida.


## Observação

- Ambos os terminais (cliente e servidor) devem estar na mesma máquina ou na mesma rede.

---

# Explicação do funcionamento da Aplicação

## 1. `key_gen.py`

### Descrição
- Este arquivo é responsável por gerar as chaves pública e privada necessárias para a criptografia assimétrica.

### Funções

#### `generate_keys()`
- **Descrição:** Gera um par de chaves RSA (pública e privada) e as salva em arquivos.
- **Importância:** A criptografia assimétrica depende de um par de chaves; sem estas chaves, a criptografia e descriptografia não podem ocorrer.

## 2. `encryption.py`

### Descrição
- Contém funções para carregar as chaves, criptografar e descriptografar mensagens.

### Funções

#### `load_keys()`
- **Descrição:** Carrega as chaves pública e privada a partir de arquivos.
- **Importância:** Necessário para obter as chaves previamente geradas para criptografia e descriptografia.

#### `encrypt_message(message, public_key)`
- **Descrição:** Criptografa uma mensagem usando a chave pública fornecida.
- **Importância:** Garante que a mensagem pode ser enviada de forma segura, pois apenas o detentor da chave privada correspondente pode descriptografá-la.

#### `decrypt_message(encrypted_message, private_key)`
- **Descrição:** Descriptografa uma mensagem criptografada usando a chave privada fornecida.
- **Importância:** Permite que o destinatário da mensagem recupere o conteúdo original da mensagem criptografada.

## 3. `server.py`

### Descrição
- Implementa o servidor TCP que recebe e descriptografa mensagens enviadas pelo cliente.

### Funções

#### `start_server()`
- **Descrição:** Inicia o servidor, aguarda conexões de clientes, e processa mensagens recebidas.
- **Importância:** Garante que o servidor está pronto para receber conexões e processar mensagens criptografadas, descriptografando-as para exibição.

## 4. `client.py`

### Descrição
- Implementa o cliente TCP que criptografa e envia mensagens para o servidor.

### Funções

#### `start_client()`
- **Descrição:** Inicia o cliente, permite que o usuário insira mensagens, criptografa essas mensagens e as envia ao servidor.
- **Importância:** Garante que as mensagens do usuário sejam enviadas de forma segura ao servidor, usando criptografia assimétrica.