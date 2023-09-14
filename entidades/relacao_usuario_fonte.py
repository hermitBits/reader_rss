# -*- coding: utf-8 -*-
"""Modulo da entidade Relação usuário e fonte
"""
from dataclasses import dataclass
from uuid import UUID


@dataclass
class RelacaoUsarioFonte:
    """Classe da entidade Relação usuário e fonte
    """
    usuario_id: UUID
    fonte_id: UUID
