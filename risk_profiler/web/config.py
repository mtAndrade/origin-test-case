import os


class ApplicationConfig:

    host: str
    port: int
    workers: int

    def __init__(self):
        self.host = os.environ.get("HOST", default="0.0.0.0")
        self.port = os.environ.get("PORT", default=8080)
        self.workers = os.environ.get("WORKERS", default=1)