from abc import ABC, abstractmethod
from entidades.relacao_usuario_fonte import RelacaoUsarioFonte
from uuid import uuid4, UUID
from typing import Dict


class IRelacaoUsuarioFonteRepositorio(ABC):
    @abstractmethod
    def save(self, relacao: RelacaoUsarioFonte): ...


class InMemoryRepositorioRelacaoUsuarioFonte(IRelacaoUsuarioFonteRepositorio):
    def __init__(
        self, dictionary_structure: Dict[UUID, RelacaoUsarioFonte] = {}
    ):
        self.dictionary_structure = dictionary_structure

    def save(self, relacao: RelacaoUsarioFonte):
        relacao_id = uuid4()
        self.dictionary_structure[relacao_id] = relacao
        return {
            'id': relacao_id,
            'id_fonte': relacao.id_fonte,
            'id_usuario': relacao.id_usuario,
        }
