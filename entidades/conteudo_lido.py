# -*- coding: utf-8 -*-
"""Modulo da entidade Conteudo Lido
"""
from dataclasses import dataclass
from uuid import UUID


@dataclass
class ConteudoLido:
    """Classe da entidade Usuário
    """
    id_usuario: UUID
    id_conteudo: UUID
    lido: bool
