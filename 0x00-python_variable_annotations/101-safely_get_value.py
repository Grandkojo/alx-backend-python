#!/usr/bin/env python3
"""More involved type annotations"""
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None],
) -> Union[Any, T]:
    """This returns keys or default"""
    if key in dct:
        return dict[key]
    else:
        return default
