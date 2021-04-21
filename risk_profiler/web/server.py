from gunicorn.app.base import BaseApplication
from aiohttp.worker import GunicornWebWorker
from risk_profiler.web.config import ApplicationConfig

class _GunicornApplication(BaseApplication):
    def __init__(self, app, config: ApplicationConfig):
        self.application = app
        self.config = config
        super().__init__()

    def load_config(self):
        self.cfg.set("bind", f"{self.config.host}:{self.config.port}")
        self.cfg.set("workers",self.config.workers)
        self.cfg.set("timeout",50000)
        self.cfg.set("worker_class", "aiohttp.worker.GunicornWebWorker")

    def load(self):
        return self.application


class GunicornServer:
    _server: _GunicornApplication

    def __init__(self, app, config):
        super().__init__()
        self._server = _GunicornApplication(app, config)

    def run(self):
        self._server.run()