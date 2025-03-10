"""Top-level package for naipromptformatter."""

__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
    "WEB_DIRECTORY",
]

__author__ = """Sijie Mei"""
__email__ = "245798972@qq.com"
__version__ = "at for noobai"

from .src.naipromptformatter.nodes import NODE_CLASS_MAPPINGS
from .src.naipromptformatter.nodes import NODE_DISPLAY_NAME_MAPPINGS

WEB_DIRECTORY = "./web"
