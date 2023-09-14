# -*- coding: utf-8 -*-
"""Modulo Core de processamento de RSS
"""
from typing import List, Dict

from requests.exceptions import RequestException
from requests_html import HTMLSession


def pegar_fonte(url):
    """Função para capturar XML feed da fonte
    
    Args:
        url (string): url da fonte
        
    Returns:
        O retorno será, HTMLSession da classe para sucesso, None para erro.
    
    """
    resposta = None
    try:
        sessao = HTMLSession()
        resposta = sessao.get(url)

        return resposta
    except RequestException as error:
        print(error)
    return resposta


def pegar_feed(url) -> List[Dict[str, str]]:
    """Função para capturar campos principais para criar um feed amigavel
    
    Args:
        url (string): url da fonte
        
    Returns:
        list: Dicionarios com conteudo para sucesso, array vazia para erro ou
        quando a fonte não tiver nenhum conteudo para lançar.
    """
    resposta = pegar_fonte(url)
    conteudos = []

    with resposta:
        items = resposta.html.find('item', first=False)

        for item in items:
            titulo = item.find('title', first=True).text
            data_publicacao = item.find('pubDate', first=True).text
            guid = item.find('guid', first=True).text
            descricao = item.find('description', first=True).text
            media = item.find('enclosure', first=True)
            descricao_completa = item.find('encoded', first=True).html

            data = {
                'titulo': titulo,
                'data_publicacao': data_publicacao,
                'guid': guid,
                'descricao': descricao,
                'media': media,
                'conteudo': descricao_completa,
            }

            conteudos.append(data)

    return conteudos
