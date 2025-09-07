from app.api.api_v1.api import api_router
from app.core.config import settings
from app.create_app import create_app

app = create_app(
    version=settings.APP_VERSION,
    router=api_router,
    router_prefix=settings.API_V1_STR,
)
