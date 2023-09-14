# -*- coding: utf-8 -*-
"""Modulo da entidade Usuário
"""
from dataclasses import dataclass
from hashlib import md5


@dataclass
class Usuario:
    """Classe da entidade Usuário
    """
    nome: str
    usuario_nome: str
    senha: str

    def __post_init__(self):
        self.senha = md5(self.senha.encode('utf8')).hexdigest()
