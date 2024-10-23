import socket

def Main():
    host = '127.0.0.1'
    port = 6787

    socketMulti = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socketMulti.connect((host, port))

    while True:
        filename = input("Digite o nome do arquivo que deseja (ou 'exit' para sair): ")
        
        socketMulti.send(f"GET /{filename} HTTP/1.1".encode('utf-8'))

        if filename.lower() == "exit":
            print("Encerrando a conexão.")
            break

        response = socketMulti.recv(4096).decode('utf-8')
        print(f'Resposta do servidor:\n{response}')

    socketMulti.close()

if __name__ == '__main__':
    Main()
