import socket
import threading
import os

def handle_client(conn, addr):
    print(f"Conexão estabelecida com IP: {addr[0]} Porta:{addr[1]}")
    
    while True:
        data = conn.recv(4096).decode('utf-8')
        if not data:
            break
        print(f"Solicitação recebida de IP: {addr[0]} Porta:{addr[1]}")
        print(f"Arquivo: {data}")
        filename = data.split()[1][1:]
        
        if filename.lower() == 'exit':
            print(f"Conexão encerrada com IP: {addr[0]} Porta:{addr[1]}")
            break
        
        folder_path = 'arquivos'
        file_path = os.path.join(folder_path, filename)
        
        try:
            with open(file_path, 'r') as file:
                content = file.read()
            response = f"HTTP/1.1 200 OK\n\n{content}"
        except FileNotFoundError:
            response = "HTTP/1.1 404 NOT FOUND\n\nArquivo não encontrado"
        
        conn.send(response.encode('utf-8'))

    conn.close()

def Main():
    host = '127.0.0.1'
    port = 6787

    socketMulti = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketMulti.bind((host, port))
    socketMulti.listen(5)

    print("Servidor aguardando conexões...")

    while True:
        conn, addr = socketMulti.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()

if __name__ == '__main__':
    Main()
