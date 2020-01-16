from django.contrib.auth.models import AbstractUser
from django.core.handlers.wsgi import WSGIRequest
from typing import Dict, Any, Union

from .models import ToListMixin


def get_base_context(request: WSGIRequest) -> Dict[str, Any]:
    user: Union[AbstractUser, ToListMixin] = request.user

    context = {
        'is_login': user.is_anonymous,
        'user': None if user.is_anonymous else {
            'name': user.to_dict()
        }
    }
    return context
