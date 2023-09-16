# -*- coding: utf-8 -*-
"""Caso de uso - criar usuãrio
"""
from dataclasses import dataclass
from uuid import UUID

from casos_de_uso.interface_casos_de_uso import ICasodeUso
from entidades.usuario import Usuario
from repositorios.usuario_repositorio import IUsuarioRepositorio


@dataclass
class CriarUsuarioSolicitar:
    nome: str
    usuario_nome: str
    senha: str


@dataclass
class CriarUsuarioResposta:
    id: UUID
    nome: str
    usuario_nome: str
    senha: str
    ativo: bool


class CasodeUsoCriarUsuario(ICasodeUso):
    
    def __init__(self, repositorio: IUsuarioRepositorio):
        self.repositorio = repositorio
    
    def execute(self, solicitar: CriarUsuarioSolicitar) -> CriarUsuarioResposta:
        novo_usuario = Usuario(
            nome=solicitar.nome,
            usuario_nome=solicitar.usuario_nome,
            senha=solicitar.senha
        )
                
        salvar_usuario = self.repositorio.save(
            usuario=novo_usuario
        )