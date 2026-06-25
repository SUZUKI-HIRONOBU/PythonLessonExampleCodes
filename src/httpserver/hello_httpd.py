# File: hello_httpd.py
## Hello World httpd server.
# Refernce # https://docs.python.org/ja/3/library/http.server.html
# 

from http.server import BaseHTTPRequestHandler
import socketserver
PORT = 8080
ADDRESS="0.0.0.0"                # 必要に応じてアドレスに制限をかける.
response_message=b"Hello World\n"

#
# HTTP/1.0で応答ごとに接続が閉じている. (1.1にはしない)
# シングルスレッドで処理する. (接続負荷の制限)
#
class LocalHandler(BaseHTTPRequestHandler):
    # タイムアウトを3秒と短くしておく.
    timeout = 5                    
    # サーバー/システムのバージョンを削除する場合
    # server_version = ''
    # sys_version= ''
    def do_GET(self):
        self._access_log(self.path,self.client_address)
        self.do_response()
    def do_HEAD(self):
        self._access_log(self.path,self.client_address)
        self.send_response(200)
        self.end_headers()
    def do_POST(self):
        self._access_log(self.path,self.client_address)
        self.send_response(403)  # POSTリクエストは常にForbiddenとして拒否
        self.send_header('Content-Length', '0')
        self.end_headers()
    def do_response(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', '{}'.format(len(response_message)))
        self.end_headers()
        self.wfile.write(response_message)
    def _access_log(self,_path,addr_port):
        # URLのパスに悪意の制御文字が入っている場合を想定しての.
        path = _path.encode('unicode_escape').decode('ascii')
        print('PATH: {}'.format(path))
        address,port = addr_port
        print('ADDRESS: {}'.format(address))
        print('PORT: {}'.format(port))
        
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer((ADDRESS, PORT), LocalHandler) as httpd:
    print('*** START Hello HTTPD ***')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print(u'\nShutdown...')
