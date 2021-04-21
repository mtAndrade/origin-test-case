from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
from aiohttp import web
from risk_profiler.web.router import Router

class BaseTestCase(AioHTTPTestCase):

    async def get_application(self):
        app = web.Application()
        Router.register("risk_profiler.resources", app.router)
        return app
