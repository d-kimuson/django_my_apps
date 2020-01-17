from django.db import models
from django.db.models.manager import BaseManager
from django.db.models.query import QuerySet
from typing import Optional, List, Dict, Any, TypeVar, Union, Type, TYPE_CHECKING
from typing_extensions import Protocol


class MixinModelProtocol(Protocol):
    pk: int
    objects: Any


class ModelProtocol(Protocol):
    pk: int
    objects: Any

    def to_dict(self) -> Dict[str, Any]: ...

    @classmethod
    def to_list(cls: Type['ModelProtocol'], *arg, **kwargs) -> List[Dict[str, Any]]: ...


class UserModelProtocol(ModelProtocol):
    is_anonymous: bool


class ToDictMixin(models.Model):
    class Meta:
        abstract = True

    def to_dict(self) -> Dict[str, Any]:
        return {
            "pk": self.pk
        }


class ToListMixin(ToDictMixin):
    class Meta:
        abstract = True

    @classmethod
    def to_list(cls: Any,
                base: Any,
                **kwargs) -> List[Dict[str, Any]]:
        base_qs = cls.objects.all() if base is None else base

        try:
            filtered = base_qs.filter(**kwargs)
        except AttributeError as e:
            print(e)
            return []

        return [inst.to_dict() for inst in filtered]
