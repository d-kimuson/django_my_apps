from django.db import models
from django.db.models import BaseManager
from django.db.models.query import QuerySet
from typing import Optional, List, Dict, Any, TypeVar, Union, Type, Protocol

from .protocols import MixinModelProtocol

QS = TypeVar('QS', BaseManager[Any], QuerySet[Any])


class ToDictMixin(MixinModelProtocol):
    def to_dict(self) -> Dict[str, Any]:
        return {
            "pk": self.pk
        }


class ToListMixin(ToDictMixin):
    @classmethod
    def to_list(cls: Type['ToListMixin'],
                base: Optional[QS] = None,
                **kwargs) -> List[Dict[str, Any]]:

        base_qs: Union[BaseManager[Any], QS] = cls.objects.all() if base is None else base

        try:
            filtered: Union[BaseManager[Any], QS] = base_qs.filter(**kwargs)
        except AttributeError as e:
            print(e)
            return []

        return [inst.to_dict() for inst in filtered]
