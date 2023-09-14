from entidades.rss_conteudo import RssConteudo
from requests.exceptions import RequestException
from requests_html import HTMLSession
from typing import List


def pegar_fonte(url):
    try: 
        sessao = HTMLSession()
        resposta = sessao.get(url)
        
        return resposta
    except RequestException as e:
        print(e)
    
        
def pegar_feed(url) -> List[RssConteudo]:
    resposta = pegar_fonte(url)
    conteudos = []
    
    with resposta as r:
        items = r.html.find('item', first=False)

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