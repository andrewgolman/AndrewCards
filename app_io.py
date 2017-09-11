from config import mode, port

if mode == 'console':
    def console_input():
        return input().strip()

    def console_output(*args, **kwargs):
        print(*args, sep='', *kwargs)

    app_input = console_input
    app_output = console_output

elif mode == 'server':

    from socket import socket

    class ServerOutput:
        def __init__(self, connection):
            self.lines = []
            self.conn = connection

        def __call__(self, *args, **kwargs):
            for i in args:
                self.lines.append(str(i))

        def flush(self):
            ans = "\n".join(self.lines)
            self.conn.send(ans.encode())
            self.lines = []

    def serv_input():
        app_output.flush()
        return conn.recv(1024).decode().strip()


    sock = socket()
    sock.bind(('', port))
    sock.listen(10)
    conn, addr = sock.accept()

    app_input = serv_input
    app_output = ServerOutput(conn)


else:
    print("RUN MODE ERROR")
