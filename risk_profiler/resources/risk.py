from risk_profiler.web.router import Router
from risk_profiler.services.risk import RiskService
from aiohttp import web
from webargs.aiohttpparser import use_args
from risk_profiler.resources.schemas.user import UserSchema
from http import HTTPStatus

@Router("/risk/profile", method="POST")
@use_args(UserSchema)
async def index(request, user):
    risk_profile = RiskService.accertain_risk_profile(user)
    return web.json_response(risk_profile)