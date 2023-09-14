# -*- coding: utf-8 -*-
"""Modulo da entidade RSS Conteudo
"""
from dataclasses import dataclass
from uuid import UUID


@dataclass
class RssConteudo:
    """Classe da entidade RSS Conteudo
    """
    id_fonte: UUID
    titulo: str
    data_publicacao: str
    guid: str
    descricao: str
    media: str
    conteudo: str
