"""
https://twistedmatrix.com/documents/current/core/howto/application.html
"""
import traceback
from twisted.internet import reactor, protocol
# from twisted.protocols.basic import NetstringReceiver


class ServerProtocol(protocol.Protocol):  # protocol.Protocol
    """This is just about the simplest possible protocol"""
    def dataReceived(self, data):
        "As soon as any data is received, write it back."
        # TODO 数据过长处理
        print('MAX_LENGTH:{}'.format(self.MAX_LENGTH))
        encode_type = 'utf8'
        print('data:{}'.format(data[:20]))
        try:
            if isinstance(data, bytes):
                print('data decode')
                encode_type, data = self._bytes_decode(data)
            print('dataReceived : {}'.format(data[:50]))
            response = data[:50]
        except Exception as e:
            traceback.print_exc()
            response = str(e)
        print('encode_type:{}'.format(encode_type))
        self.transport.write(response.encode(encoding=encode_type))

    def connectionLost(self, reason):
        print('client : {} disconnected'.format(self.transport.client))
        print('disconnected reason:{}'.format(reason))

    def connectionMade(self):
        """客户端连入后向客户端发送一条消息Hello"""
        print('MAX_LENGTH:{}'.format(self.MAX_LENGTH))
        print('MAX_LENGTH:{}'.format(self.MAX_LENGTH))
        print('client : {} connected'.format(self.transport.client))
        self.transport.write("connected success".encode(encoding='utf8'))

    def _bytes_decode(self, recv_bytes):
        """解码"""
        encode_type = 'utf8'
        try:
            recv = recv_bytes.decode(encoding="utf8")
        except Exception:
            try:
                recv = recv_bytes.decode(encoding="gbk")
                encode_type = 'gbk'
            except Exception:
                raise Exception('need utf8 or gbk encode')
        return encode_type, recv


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
