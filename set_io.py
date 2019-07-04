from config import mode, port, uuid
from config import buffer
from socket import socket


if mode == 'console':
    def console_input():
        return input().strip()

    def console_output(*args, **kwargs):
        print(*args, sep='', **kwargs)

    app_input = console_input
    app_output = console_output


elif mode == 'server':
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


elif mode == 'bot':
    def bot_input():
        s = yield
        return s

    def bot_output(id=uuid, *args, **kwargs):
        buffer[id].append(''.join(args))

    app_output = bot_output

else:
    raise RuntimeError("RUN MODE ERROR")
