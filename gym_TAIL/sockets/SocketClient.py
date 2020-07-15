import socket

from .SocketData import SocketData
from .SocketListener import SocketListener
from .SocketWorker import SocketWorker


class SocketClient():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener = None
    connected = False
    worker = None

    def __init__(self, host, port):
        self.port = port
        self.host = host
        self.listener = SocketListener()
        self.connect()

    def send(self, message=None, channel="$MESSAGE"):
        data = SocketData(str(message), channel)
        self.sock.sendall((data.serialize() + "\n").encode())

    def connect(self):
        if not self.connected:
            self.sock.connect((self.host, self.port))
            self.connected = True
            self.worker = SocketWorker(self.sock, self.listener)
            self.worker.start()

    def disconnect(self):
        if self.connected:
            try:
                self.send('bye', "$DISCONNECT")
                self.sock.close()
            finally:
                self.connected = False

    def on(self, channel, observer):
        self.listener.register(channel, observer)
