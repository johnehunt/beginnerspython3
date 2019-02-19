import socket


def get_input():
    message = 'Please provide an input (Date, Time, DataAndTime or -1 to exit): '
    return input(message)


def main():
    print('Starting Client')
    user_input = get_input()
    while user_input != '-1':
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(('localhost', 8080))
            print('Connected to server')
            print('Sending data')
            sock.send(user_input.encode())
            data = sock.recv(1024).decode()
            print('Received from server: ', data)
        finally:
            print('Closing socket')
            sock.close()
        user_input = get_input()


if __name__ == '__main__':
    main()
