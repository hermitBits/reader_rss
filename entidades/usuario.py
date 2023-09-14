# -*- coding: utf-8 -*-
"""Modulo da entidade Usuário
"""
from dataclasses import dataclass


@dataclass
class Usuario:
    """Classe da entidade Usuário
    """
    nome: str
    usuario_nome: str
    senha: str
