from aiohttp import web
from .config import ApplicationConfig
from .server import GunicornServer
from risk_profiler.web.router import Router

class Application:
    
    config: ApplicationConfig

    def __init__(self):
        self.config = ApplicationConfig()

    def run(self):
        app = web.Application()
        Router.register("risk_profiler.resources", app.router)

        server = GunicornServer(app, self.config)
        server.run()

def build():
    return Application()