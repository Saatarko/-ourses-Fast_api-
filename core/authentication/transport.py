
# это трансопрт (т.е где будет переджватсья токен)_
from fastapi_users.authentication import BearerTransport

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")