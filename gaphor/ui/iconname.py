"""
With `get_icon_name` you can retrieve an icon name
for a model element.
"""

import re
from functools import singledispatch

TO_KEBAB = re.compile(r"([a-z])([A-Z]+)")


def to_kebab_case(s):
    return TO_KEBAB.sub("\\1-\\2", s).lower()


@singledispatch
def get_icon_name(element):
    """
    Get an icon name for a model element.
    """
    return f"gaphor-{to_kebab_case(element.__class__.__name__)}-symbolic"
