import base64

class SocketData ():
    channel = ""
    message = ""

    def __init__(self, message, channel="$MESSAGE"):
        self.channel = channel
        self.message = message

    @staticmethod
    def parse(data):
        decoded = base64.decodebytes(data).decode()
        channel, message = decoded.split(':', 1)
        return SocketData(message, channel)

    def serialize(self):
        return base64.b64encode((self.channel + ":" + str(self.message)).encode()).decode()

    def __str__(self):
        message = ""
        if (self.message is None):
            message = "$NULL"
        else:
            message = self.message.encode()
        return self.channel + ": " + str(message)