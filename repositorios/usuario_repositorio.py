# -*- coding: utf-8 -*-
"""Modulo do repositorio de Usuario
"""
from abc import ABC, abstractmethod
from uuid import uuid4, UUID
from typing import Dict, List

from entidades.usuario import Usuario


class IUsuarioRepositorio(ABC):
    """Interface para classe do repositorio implementar
    """

    @abstractmethod
    def save(self, usuario: Usuario) -> Usuario:
        """Método para salvar no repositorio

        Args:
            usuario (Usuario): objecto de Usuario

        Returns:
            Usuario: Objeto Usuario
        """

    @abstractmethod
    def get_by_id(self, usuario: UUID) -> Usuario:
        """Método pesquisar uma usuários
        
        Args:
            usuario (UUID): UUID para pesquisar no repositório
        
        Returns:
            RssFonte: retorna uma objeto de usuario
        """

    @abstractmethod
    def delete(self, usuario: str) -> bool:
        """Método para deletar um usuário
        
        Args:
            usuario (UUID): UUID para pesquisar no repositório
        
        Returns:
            bool: True para sucesso
        """

    @abstractmethod
    def get_all(self) -> List[Usuario]:
        """Função para pegar todos usuários

        Returns:
            list: lista de Usuario
        """


class InMemoryRepositorioUsuario(IUsuarioRepositorio):
    """Classe que implementa repositorio em memoria dos usuarios
    """
    def __init__(self, dictionary_structure: Dict[UUID, Usuario] = None):
        self.dictionary_structure = dictionary_structure

    def save(self, usuario: Usuario):
        usuario.set_id(uuid4())
        self.dictionary_structure[usuario.id] = usuario
        return usuario

    def delete(self, usuario: str): ...

    def get_all(self):
        return list(self.dictionary_structure.items())

    def get_by_id(self, usuario: UUID): ...
