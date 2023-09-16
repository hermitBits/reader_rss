# -*- coding: utf-8 -*-
"""Modulo da entidade RSS Fonte
"""
from dataclasses import dataclass
from uuid import UUID


@dataclass
class RssFonte:
    """Classe da entidade RSS Fonte
    """
    nome: str
    url: str
    ativo: bool = True
    _id: UUID = None

    def set_id(self, _id):
        """Atribuir id á entidade
        """
        self._id = _id

    @property
    def id(self):
        """Acessar o valor ID
        """
        return self._id
