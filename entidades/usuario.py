# -*- coding: utf-8 -*-
"""Modulo da entidade Usuário
"""
from dataclasses import dataclass
from hashlib import md5
from uuid import UUID


@dataclass
class Usuario:
    """Classe da entidade Usuário
    """
    nome: str
    usuario_nome: str
    senha: str
    ativo: bool = True
    _id: UUID = None

    def __post_init__(self):
        self.senha = md5(self.senha.encode('utf8')).hexdigest()

    def set_id(self, _id):
        """Atribuir id á entidade
        """
        self._id = _id

    @property
    def id(self):
        """Acessar o valor ID
        """
        return self._id
