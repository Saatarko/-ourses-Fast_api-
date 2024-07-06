from fastapi_users.authentication import BearerTransport

from core.config import settings


# это трансопрт (т.е где будет переджватсья токен)_
bearer_transport = BearerTransport(
    tokenUrl=settings.api.bearer_token_url,
)
