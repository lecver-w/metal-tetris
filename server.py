import http.server
import socketserver
import os
import sys

PORT = 8080
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class ResilientHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def do_GET(self):
        # 兼容用户在手机端输入各种可能的子路径，例如 /metal-tetris, /tetris 等
        for prefix in ['/metal-tetris', '/tetris', '/game']:
            if self.path.startswith(prefix):
                self.path = self.path[len(prefix):]
                if not self.path:
                    self.path = '/'
                break
        
        # 如果访问的是不存在的文件且是页面请求，自动重定向到 index.html
        super().do_GET()

    def end_headers(self):
        # 允许跨域与防止某些移动端浏览器缓存异常
        self.send_header('Cache-Control', 'no-cache, must-revalidate')
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

if __name__ == '__main__':
    # 支持命令行指定端口，默认 8080
    if len(sys.argv) > 1:
        try:
            PORT = int(sys.argv[1])
        except ValueError:
            pass

    # 允许端口快速复用，避免重启时提示 Address already in use
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), ResilientHandler) as httpd:
        print(f"Server started at port {PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
