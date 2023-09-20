# -*- coding: utf-8 -*-
"""Caso de uso - criar usuãrio
"""
from dataclasses import dataclass
from uuid import UUID

from casos_de_uso.interface_casos_de_uso import ICasodeUso
from casos_de_uso.usuario.todos_usuario import CasodeUsoTodosUsuario
from casos_de_uso.usuario.usuario_errors import SenhaCurta, UsuarioNomeJaExiste

from entidades.usuario import Usuario

from repositorios.usuario_repositorio import IUsuarioRepositorio


@dataclass
class CriarUsuarioSolicitar:
    """Classe de socilitar para criar um usuario
    """
    nome: str
    usuario_nome: str
    senha: str


@dataclass
class CriarUsuarioResposta:
    """Classe de resposta para criar um usuario
    """
    nome: str
    usuario_nome: str
    senha: str
    ativo: bool


class CasodeUsoCriarUsuario(ICasodeUso):
    """_Caso de uso para criação de um usuario

    Args:
        repositorio (IUsuarioRepositorio): criar caso de uso
    """

    def __init__(self, repositorio: IUsuarioRepositorio):
        self.repositorio = repositorio

    def execute(self, solicitar: CriarUsuarioSolicitar) -> CriarUsuarioResposta:
        novo_usuario = Usuario(
            nome=solicitar.nome,
            usuario_nome=solicitar.usuario_nome,
            senha=solicitar.senha
        )

        self.check_usuario_nome_existe(novo_usuario.usuario_nome)
        self.check_tamanho_senha(solicitar.senha)

        return self.repositorio.save(
            usuario=novo_usuario
        )

    def check_tamanho_senha(self, senha):
        if len(senha) <= 5:
            raise SenhaCurta
        return True

    def check_usuario_nome_existe(self, usuario_nome):
        todos_usuarios = CasodeUsoTodosUsuario(
            repositorio=self.repositorio
        ).execute()

        for usuario in todos_usuarios.items:
            if usuario_nome == usuario[1].usuario_nome:
                raise UsuarioNomeJaExiste
        return True
