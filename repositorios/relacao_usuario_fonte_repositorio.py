# -*- coding: utf-8 -*-
"""Modulo do repositorio de Relação entre usuarios e fonte
"""
from abc import ABC, abstractmethod
from uuid import uuid4, UUID
from typing import Dict

from entidades.relacao_usuario_fonte import RelacaoUsarioFonte


class IRelacaoUsuarioFonteRepositorio(ABC):
    """Interface para classe do repositorio implementar
    """

    @abstractmethod
    def save(self, relacao: RelacaoUsarioFonte):
        """Método para salvar no repositorio
        
        Args:
            relacao (RelacaoUsarioFonte): objecto de uma Relação entre fonte e usuario
        
        Returns:
            dict: Dicionário com id, fonte_id e usuario_id para sucesso.
        """

    @abstractmethod
    def get_by_id(self, relacao_id: UUID):
        """Método pesquisar uma relação
        
        Args:
            relacao_id (UUID): UUID para pesquisar no repositório
        
        Returns:
            RelacaoUsarioFonte: retorna uma objeto de relação
        """

    @abstractmethod
    def delete(self, relacao_id: str):
        """Método para deletar uma relação
        
        Args:
            relacao (RelacaoUsarioFonte): objecto de uma Relação entre fonte e usuario
        
        Returns:
            dict: Dicionário com id, fonte_id e usuario_id para sucesso.
        """

    @abstractmethod
    def get_all(self, relacao_id: str):
        """Função para capturar XML feed da fonte
        
        Args:
            relacao (RelacaoUsarioFonte): objecto de uma Relação entre fonte e usuario
        
        Returns:
            dict: Dicionário com id, fonte_id e usuario_id para sucesso.
        """


class InMemoryRepositorioRelacaoUsuarioFonte(IRelacaoUsuarioFonteRepositorio):
    """Class que implementa repositorio em memoria das relações
    """

    def __init__(
        self, dictionary_structure: Dict[UUID, RelacaoUsarioFonte] = None
    ):
        self.dictionary_structure = dictionary_structure

    def save(self, relacao: RelacaoUsarioFonte):
        relacao_id = uuid4()
        self.dictionary_structure[relacao_id] = relacao
        return {
            'id': relacao_id,
            'fonte_id': relacao.fonte_id,
            'usuario_id': relacao.usuario_id,
        }
