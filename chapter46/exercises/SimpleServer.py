import socketserver
from datetime import datetime, date


class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        print('In Handle')
        # Obtain inpout data
        data = self.request.recv(1024).decode()
        print('data received:', data)
        request = str(data).upper()
        if request == 'DATE':
            response = str(date.today())
        elif request == 'TIME':
            now = datetime.now()
            response = now.strftime("%H:%M:%S")
        elif request == 'DATEANDTIME':
            response = str(datetime.today())
        else:
            response = 'UNKNOWN OPTION:' + request

        print('response:', response)

        # Send the result back to the client
        self.request.sendall(response.encode())


def main():
    print('Starting')
    address = ('localhost', 8080)
    server = socketserver.ThreadingTCPServer(address,
                                MyTCPHandler)
    print('Activating server')
    server.serve_forever()


if __name__ == '__main__':
    main()
