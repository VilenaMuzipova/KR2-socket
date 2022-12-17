import socket


def start_server():
    host = "127.0.0.1"
    port = 4000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))

    s.listen(1)
    print("сервер запущен")
    print("ожидание запроса клиента..")

    conn, address = s.accept()
    print(f'Connected user: {address}')
    message = ''


    while True:
        data = conn.recv(1024)
        message = data.decode()
        if message == 'Over':
            print('соединение завершено')
            break
        print('уравнение получено')
        result = 0
        operation_list = message.split()
        oprnd1 = operation_list[0]
        operation = operation_list[1]
        oprnd2 = operation_list[2]

        num1 = int(oprnd1)
        num2 = int(oprnd2)

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2

        print ('отправить результат')

        output = str(result)
        client = str(result)
        conn.send(output.encode())
    conn.close()


if __name__ == '__main__':
    start_server()
