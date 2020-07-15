import threading

from .SocketData import SocketData

class SocketWorker (threading.Thread):
    socket = None
    listener = None
    def __init__(self, socket, listener):
        super().__init__()
        self.socket = socket
        self.listener = listener

    def waitForResponse(self): #->Bytes
        res = b''
        while True:
            try:
                _in = self.socket.recv(1)
                if _in.decode() == "\n":
                    break
                else:
                    res += _in
            except Exception as err:
                self.listener.notify(SocketData(None, "$DISCONNECT"))
                quit()
        return res
    
    def run(self):
        while True:
            encoded = self.waitForResponse()
            try:
                data = SocketData.parse(encoded)
                self.listener.notify(data)
            except Exception as err:
                raise err
                break
        print("worker thread quit after internal exception")