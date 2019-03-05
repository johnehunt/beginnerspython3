import socket


def main():
    # Setup names and offices
    addresses = {'JOHN': 'C45',
                 'DENISE': 'C44',
                 'PHOEBE': 'D52',
                 'ADAM': 'B23'}

    print('Starting Server')
    print('Create the socket')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print('Bind the socket to the port')
    server_address = (socket.gethostname(), 8084)
    print('Starting up on', server_address)
    sock.bind(server_address)

    # specifies the number of connections
    # before refusing new connections.
    print('Listen for incoming connections')
    sock.listen(1)
    while True:
        print('Waiting for a connection')
        connection, client_address = sock.accept()
        try:
            print('Connection from', client_address)
            while True:
                data = connection.recv(1024).decode()
                print('Received: ', data)
                if data:
                    key = str(data).upper()
                    response = addresses[key]
                    print('sending data back to the client: ',
                          response)
                    connection.sendall(response.encode())
                else:
                    print('No more data from', client_address)
                    break
        finally:
            connection.close()


if __name__ == '__main__':
    main()
