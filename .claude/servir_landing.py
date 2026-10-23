"""Servidor local da landing page, usado pela skill conferir-visual.

Diferente de `python -m http.server`, só entrega arquivos da página
(HTML, CSS, JS, imagens e fontes). Arquivos e pastas que começam com
ponto (.env, .git, .claude) e listagem de diretório ficam bloqueados.
"""
import http.server
import os
import sys
from urllib.parse import unquote, urlsplit

PORTA = int(sys.argv[1]) if len(sys.argv) > 1 else 8123
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PERMITIDAS = {
    ".html", ".css", ".js",
    ".svg", ".png", ".jpg", ".jpeg", ".webp", ".gif", ".ico", ".avif",
    ".woff", ".woff2",
}


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=RAIZ, **kwargs)

    def permitido(self):
        caminho = unquote(urlsplit(self.path).path)
        if caminho.endswith("/"):
            caminho += "index.html"
        partes = [p for p in caminho.replace("\\", "/").split("/") if p]
        if any(p.startswith(".") for p in partes):
            return False
        return os.path.splitext(caminho)[1].lower() in PERMITIDAS

    def do_GET(self):
        if not self.permitido():
            self.send_error(404)
            return
        super().do_GET()

    def do_HEAD(self):
        if not self.permitido():
            self.send_error(404)
            return
        super().do_HEAD()


if __name__ == "__main__":
    servidor = http.server.ThreadingHTTPServer(("127.0.0.1", PORTA), Handler)
    print("Servindo a landing em http://localhost:%d/" % PORTA, flush=True)
    servidor.serve_forever()
