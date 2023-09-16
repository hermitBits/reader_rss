# -*- coding: utf-8 -*-
"""Modulo do repositorio de RSS Fonte
"""
from abc import ABC, abstractmethod
from uuid import uuid4, UUID
from typing import Dict, List

from entidades.rss_fonte import RssFonte


class IRSSFonteRepositorio(ABC):
    """Interface para classe do repositorio implementar
    """

    @abstractmethod
    def save(self, rss_fonte: RssFonte) -> RssFonte:
        """Método para salvar no repositorio
        
        Args:
            rss_fonte (RssFonte): objecto de RssFonte
        
        Returns:
            RssFonte: objeto RssFonte
        """

    @abstractmethod
    def get_by_id(self, rss_fonte_id: UUID) -> RssFonte:
        """Método pesquisar uma rss fonte
        
        Args:
            rss_fonte_id (UUID): UUID para pesquisar no repositório
        
        Returns:
            RssFonte: retorna uma objeto de rss fonte
        """

    @abstractmethod
    def delete(self, rss_fonte_id: str) -> bool:
        """Método para deletar uma rss fonte
        
        Args:
            rss_fonte_id (UUID): UUID para pesquisar no repositório
        
        Returns:
            bool: True para sucesso
        """

    @abstractmethod
    def get_all(self) -> List[RssFonte]:
        """Função para pegar todos rss fontes

        Returns:
            list: lista de RssFonte
        """


class InMemoryRepositorioRSSFonte(IRSSFonteRepositorio):
    """Classe que implementa repositorio em memoria das fontes rss
    """

    def __init__(self, dictionary_structure: Dict[UUID, RssFonte] = None):
        self.dictionary_structure = dictionary_structure

    def save(self, rss_fonte: RssFonte):
        rss_fonte.set_id(uuid4())
        self.dictionary_structure[rss_fonte.id] = rss_fonte
        return rss_fonte

    def delete(self, rss_fonte_id: str): ...

    def get_all(self): ...

    def get_by_id(self, rss_fonte_id: UUID): ...
