class SocketRegister:
    sockets = set()

    @staticmethod
    def register(socket):
        SocketRegister.sockets.add(socket)

    @staticmethod
    def get(index):
        return list(SocketRegister.sockets)[index]
