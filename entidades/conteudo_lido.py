# -*- coding: utf-8 -*-
"""Modulo da entidade Conteudo Lido
"""
from dataclasses import dataclass
from uuid import UUID


@dataclass
class ConteudoLido:
    """Classe da entidade Usuário
    """
    usuario_id: UUID
    conteudo_id: UUID
    lido: bool
