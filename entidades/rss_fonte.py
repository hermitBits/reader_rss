# -*- coding: utf-8 -*-
"""Modulo da entidade RSS Fonte
"""
from dataclasses import dataclass


@dataclass
class RssFonte:
    """Classe da entidade RSS Fonte
    """
    nome: str
    url: str
