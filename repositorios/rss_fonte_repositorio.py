# -*- coding: utf-8 -*-
"""Modulo do repositorio de Relação entre usuarios e fonte
"""
from abc import ABC, abstractmethod
from uuid import uuid4, UUID
from typing import Dict

from entidades.rss_fonte import RssFonte


class IRSSFonteRepositorio(ABC):
    """Interface para classe do repositorio implementar
    """

    @abstractmethod
    def save(self, rss_fonte: RssFonte):
        """Método para salvar no repositorio
        
        Args:
            rss_fonte (RssFonte): objecto de RssFonte
        
        Returns:
            dict: Dicionário com id e url
        """

    @abstractmethod
    def get_by_id(self, rss_fonte_id: UUID):
        """Método pesquisar uma rss fonte
        
        Args:
            rss_fonte_id (UUID): UUID para pesquisar no repositório
        
        Returns:
            RssFonte: retorna uma objeto de rss fonte
        """

    @abstractmethod
    def delete(self, rss_fonte_id: str):
        """Método para deletar uma rss fonte
        
        Args:
            rss_fonte_id (UUID): UUID para pesquisar no repositório
        
        Returns:
            bool: True para sucesso
        """

    @abstractmethod
    def get_all(self):
        """Função para capturar XML feed da fonte

        Returns:
            list: lista de RssFonte
        """


class InMemoryRepositorioRSSFonte(IRSSFonteRepositorio):
    """Class que implementa repositorio em memoria das relações
    """

    def __init__(self, dictionary_structure: Dict[UUID, RssFonte] = None):
        self.dictionary_structure = dictionary_structure

    def save(self, rss_fonte: RssFonte):
        rss_fonte_id = uuid4()
        self.dictionary_structure[rss_fonte_id] = rss_fonte
        return {
            'id': rss_fonte_id,
            'url': rss_fonte.url,
        }
