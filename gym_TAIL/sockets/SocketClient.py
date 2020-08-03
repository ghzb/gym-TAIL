import socket
import sys
import os

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

    def finish(self, caught=False):
        try:
            if not caught:
                print("TRYING TO DISCONNECT")
                self.send('bye', "$DISCONNECT")
                self.sock.close()
        finally:
            print("joining worker thread")
            self.connected = False
            self.worker.kill()
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)

    def send(self, message=None, channel="$MESSAGE"):
        try:
            data = SocketData(str(message), channel)
            self.sock.sendall((data.serialize() + "\n").encode())
        except BrokenPipeError as err:
            print("BROKEN PIPE ERROR")
            self.finish(caught=True)



    def connect(self):
        if not self.connected:
            self.sock.connect((self.host, self.port))
            self.connected = True
            self.worker = SocketWorker(self.sock, self.listener)
            self.worker.name = "python_SOCKET_WORKER"
            self.worker.start()

    def disconnect(self):
        self.finish()

    def on(self, channel, observer):
        self.listener.register(channel, observer)
