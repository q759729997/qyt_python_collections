import logging
import json
import traceback
from tornado.ioloop import IOLoop
from tornado import gen
from tornado.iostream import StreamClosedError
from tornado.tcpserver import TCPServer
from tornado.options import options, define
from tornado.iostream import IOStream

define("port", default=18000, help="TCP port to listen on")
logger = logging.getLogger(__name__)
BUFFER_SIZE = 10*1024*1024


class EchoServer(TCPServer):
    @gen.coroutine
    def handle_stream(self, stream, address):
        while True:
            try:
                received_bytes = stream.read_bytes(num_bytes=BUFFER_SIZE)
                logger.info("Received bytes len: %s", len(received_bytes))
                logger.info("Received bytes: %s", received_bytes[:50])
                stream.write('data'.encode(encoding='utf8'))
            except StreamClosedError:
                logger.warning("Lost client at host %s", address[0])
                stream.write("client closed".encode(encoding='utf8'))
                break
            except Exception as e:
                traceback.print_exc()
                response_data = {'success': False, 'Object': 'exception:' + str(e)}
                stream.write(json.dumps(response_data).encode(encoding='utf8'))


if __name__ == "__main__":
    options.parse_command_line()
    server = EchoServer()
    server.listen(options.port)
    logger.info("Listening on TCP port %d", options.port)
    IOLoop.current().start()
