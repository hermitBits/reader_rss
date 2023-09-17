# -*- coding: utf-8 -*-
"""Caso de uso - criar usuãrio
"""
from dataclasses import dataclass
from typing import List, Tuple
from uuid import UUID

from casos_de_uso.interface_casos_de_uso import ICasodeUso
from entidades.usuario import Usuario
from repositorios.usuario_repositorio import IUsuarioRepositorio


@dataclass
class TodosUsuarioResposta:
    """Classe de resposta para criar um usuario
    """
    items: List[Tuple[UUID, Usuario]]
    length: int


@dataclass
class CasodeUsoTodosUsuario(ICasodeUso):
    """_Caso de uso para criação de um usuario

    Args:
        repositorio (IUsuarioRepositorio): criar caso de uso
    """

    def __init__(self, repositorio: IUsuarioRepositorio):
        self.repositorio = repositorio

    def execute(self) -> TodosUsuarioResposta:
        response = TodosUsuarioResposta(
            items=self.repositorio.get_all(),
            length=len(self.repositorio.get_all())
        )
        return response
