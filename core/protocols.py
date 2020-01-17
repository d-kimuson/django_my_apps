from django.db.models import BaseManager
from typing import List, Dict, Any, Union, Type, Protocol


# class QSProtocol(Protocol):
#     def __iter__(self, *arg, **kwargs) -> Any: ...
#
#     def all(self, *arg, **kwargs) -> _QS: ...
#
#     def filter(self, *arg, **kwargs) -> _QS: ...
#
#     def get(self, *arg, **kwargs) -> Any: ...


class MixinModelProtocol(Protocol):
    pk: int
    objects: BaseManager[Any]


class ModelProtocol(Protocol):
    pk: int
    objects: BaseManager[Any]

    def to_dict(self) -> Dict[str, Any]: ...

    @classmethod
    def to_list(cls: Type['ModelProtocol'], *arg, **kwargs) -> List[Dict[str, Any]]: ...


class UserModelProtocol(ModelProtocol):
    is_anonymous: bool
