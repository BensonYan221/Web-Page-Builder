"""
Author: Benson
"""
from dataclasses import dataclass
from typing import List


@dataclass
class Image:
    src: str
    width: str


@dataclass
class Paragraph:
    title: str
    content: str
    images: List[Image]


@dataclass
class HTML:
    title: str
    body: List[Paragraph]
