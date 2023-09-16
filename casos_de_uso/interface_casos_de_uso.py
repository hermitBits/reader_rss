# -*- coding: utf-8 -*-
"""Interface para caso de uso
"""
from abc import ABC, abstractmethod




class ICasodeUso(ABC):
    """Classe da interface de caso de uso
    """
    
    @abstractmethod
    def __init__(self, repositorio): ...
    
    @abstractmethod
    def execute(self, solicitar): ...