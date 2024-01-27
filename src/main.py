from fastapi import FastAPI, Request, HTTPException
from starlette.status import HTTP_401_UNAUTHORIZED

from src.auth.services import api_key_auth
from src.pets.routers import router as router_pet
from src.config import API_KEY

app = FastAPI(
    title="Accounting for pets"
)

# class ApiKeyCheckerMiddleware:
#     def __init__(self, app):
#         self.app = app
#     async def __call__(self, scope, receive, send):
#         request = Request(scope, receive=receive)
#         api_key = request.headers.get("X-API-KEY")
#         if api_key != API_KEY:
#             raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Unauthorized")
#         response = await self.app(scope, receive, send)
#         return response
#
#
# app.add_middleware(ApiKeyCheckerMiddleware)

# app.add_api_route('/', router_pet, decorators=[api_key_auth])
app.include_router(router_pet)
