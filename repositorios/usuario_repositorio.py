from abc import ABC, abstractmethod
from entidades.usuario import Usuario
from uuid import uuid4, UUID
from typing import Dict


class IUsarioRepositorio(ABC):
    @abstractmethod
    def save(self, usuario: Usuario): ...


class InMemoryRepositorioUsuario(IUsarioRepositorio):
    def __init__(self, dictionary_structure: Dict[UUID, Usuario] = {}):
        self.dictionary_structure = dictionary_structure

    def save(self, usuario: Usuario):
        usuario_id = uuid4()
        self.dictionary_structure[usuario_id] = usuario
        return {
            'id': usuario_id,
            'nome': usuario.nome,
            'usuario_nome': usuario.usuario_nome
        }
