from typing import Dict, Any
from .model_modules import UserModelProtocol


def get_base_context(request: Any) -> Dict[str, Any]:
    user: UserModelProtocol = request.user

    context = {
        'is_login': user.is_anonymous,
        'user': None if user.is_anonymous else {
            'name': user.to_dict()
        }
    }
    return context
