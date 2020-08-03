import threading
import socket as s
from .SocketData import SocketData
import sys
import os

class SocketWorker (threading.Thread):
    socket = None
    listener = None
    shouldQuit = False
    def __init__(self, socket:s.socket, listener):
        super().__init__()
        self.name = "python_SOCKET_WORKER"
        self.socket = socket
        self.listener = listener

    def waitForResponse(self): #->Bytes
        res = b''
        while not self.shouldQuit:
            try:
                _in = self.socket.recv(1)

                # while _in == b'' and not self.shouldQuit:
                #     _in = self.socket.recv(1)
                #
                # if self.shouldQuit:
                #     self._kill_thread()
                # print("polled... ", _in)
                if _in.decode() == "\n":
                    break
                else:
                    res += _in

            except Exception as err:
                self._kill_thread()
        return res

    def _kill_thread(self):
        try:
            self.socket.close()
        finally:
            sys.exit()

    def kill(self):
        print("trying to quit")
        self.shouldQuit = True
        # sys.exit()

    def run(self):
        while True:
            encoded = self.waitForResponse()
            try:
                data = SocketData.parse(encoded)
                self.listener.notify(data)
            except Exception as err:
                self._kill_thread()
        # print("worker thread quit after internal exception")