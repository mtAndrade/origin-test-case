import importlib
import pkgutil


class Router:
    _routes = []

    def __init__(self, route, method="GET"):
        self.route = route
        self.method = method

    def __call__(self, fn):
        Router._routes.append((self.method, self.route, fn))
        return fn

    @classmethod
    def register(cls, path, engine):
        cls._load_modules(path)
        for method, route, handler in cls._routes:
            engine.add_route(method, route, handler)

    @classmethod
    def _load_modules(cls, path):
        channel_module = importlib.import_module(path)
        packages = []

        for _, modname, ispkg in pkgutil.iter_modules(path=channel_module.__path__):
            module_fqdn = f"{path}.{modname}"

            if ispkg:
                cls._load_modules(module_fqdn)
            else:
                packages.append(module_fqdn)

        for module_fqdn in packages:
            importlib.import_module(module_fqdn)