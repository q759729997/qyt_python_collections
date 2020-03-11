# -*- encoding=utf-8 -*-
import datetime
import socketserver
import json
import traceback

start_time = datetime.datetime.now()
BUFFER_SIZE = 10*1024*1024


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        global server
        while True:
            recv = self.request.recv(BUFFER_SIZE)
            print('recv len:{}'.format(len(recv)))
            print('recv example:{}'.format(recv[:50]))
            if len(recv) > 0:
                recv = self._bytes_decode(recv.strip())
                try:
                    recv_json = json.loads(recv)
                    print('image:{}'.format(recv_json.get('image', '')[:50]))
                    self.request.sendall("res".encode("utf8"))
                except Exception as e:
                    traceback.print_exc()
                    self.request.sendall(str(e).encode("utf8"))
            else:
                self.request.sendall("request is none".encode("utf8"))

    def _bytes_decode(self, recv_bytes):
        """解码"""
        try:
            recv = recv_bytes.decode(encoding="utf8")
        except Exception:
            try:
                recv = recv_bytes.decode(encoding="gbk")
            except Exception as e:
                raise e
        return recv


if __name__ == '__main__':
    HOST, PORT = "127.0.0.1", 18000
    socketserver.TCPServer.allow_reuse_address = True
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    end_time = datetime.datetime.now()
    print("server started in %ds." % (end_time - start_time).seconds)
    server.serve_forever()
