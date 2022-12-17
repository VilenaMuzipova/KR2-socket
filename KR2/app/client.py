import socket


def start_client():
    host = "127.0.0.1"
    port = 4000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    while True:
        print('пример: 4+5')
        inp = input(' Введите операцию:')
        if inp == 'Over':
            break

        s.send(inp.encode())
        answer = s.recv(1024).decode()
        print(f'Ответ:{answer}')
        print("Введите 'Over' чтобы завершить ")

    s.close()



if __name__ == '__main__':
    start_client()
