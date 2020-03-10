# https://twistedmatrix.com/documents/current/core/howto/application.html
import traceback
from twisted.internet import reactor, protocol


class ServerProtocol(protocol.Protocol):
    """This is just about the simplest possible protocol"""
    def dataReceived(self, data):
        "As soon as any data is received, write it back."
        # TODO 数据过长处理
        print('data:{}'.format(data[:20]))
        try:
            if isinstance(data, bytes):
                print('data decode')
                data = data.decode('utf8')
            print('dataReceived : {}'.format(data[:50]))
            response = data[:50]
        except Exception:
            traceback.print_exc()
            response = 'need utf8 encode'
        self.transport.write(response.encode(encoding='utf8'))

    def connectionLost(self, reason):
        print('client : {} disconnected'.format(self.transport.client))
        print('disconnected reason:{}'.format(reason))

    def connectionMade(self):
        """客户端连入后向客户端发送一条消息Hello"""
        print('client : {} connected'.format(self.transport.client))
        self.transport.write("connected success".encode(encoding='utf8'))


def main():
    """This runs the protocol on port 8000"""
    factory = protocol.ServerFactory()
    factory.protocol = ServerProtocol
    reactor.listenTCP(18000, factory)
    print('localhost:{}'.format(18000))
    reactor.run()


# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()
