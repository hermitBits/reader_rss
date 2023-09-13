from abc import ABC, abstractmethod
from entidades.rss_fonte import RssFonte
from uuid import uuid4, UUID
from typing import Dict


class IRSSFonteRepositorio(ABC):
    @abstractmethod
    def save(self, rss_fonte: RssFonte): ...


class InMemoryRepositorioRSSFonte(IRSSFonteRepositorio):
    def __init__(self, dictionary_structure: Dict[UUID, RssFonte] = {}):
        self.dictionary_structure = dictionary_structure

    def save(self, rss_fonte: RssFonte):
        rss_fonte_id = uuid4()
        self.dictionary_structure[rss_fonte_id] = rss_fonte
        return {
            'id': rss_fonte_id,
            'url': rss_fonte.url,
        }
