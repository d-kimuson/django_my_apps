from django.db import models
from django.db.models.query import QuerySet
from typing import Optional, List, Dict, Iterator, Any, TypeVar, Generic, Union

_Z = TypeVar("_Z")


class QueryType(Generic[_Z], QuerySet):
    def __iter__(self) -> Iterator[_Z]:
        pass


class ToListMixin(models.Model):
    def to_dict(self) -> Dict[str, Any]:
        return {
            "pk": self.pk
        }

    @classmethod
    def to_list(cls: Union[models.Model, 'ToListMixin'],
                base: Optional[QueryType[Union[models.Model, 'ToListMixin']]] = None,
                **kwargs) -> List[Dict[str, Any]]:
        base_qs: QueryType[Union[models.Model, 'ToListMixin']] = cls.objects.all() if base is None else base

        try:
            filtered: QueryType[Union[models.Model, 'ToListMixin']] = base_qs.filter(**kwargs)
        except AttributeError as e:
            print(e)
            return []

        return [inst.to_dict() for inst in filtered]
