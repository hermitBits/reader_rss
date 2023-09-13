from requests.exceptions import RequestException
from requests_html import HTMLSession


def pegar_fonte(url):
    try: 
        sessao = HTMLSession()
        resposta = sessao.get(url)
        
        return resposta
    except RequestException as e:
        print(e)
    
        
def pegar_feed(url):
    resposta = pegar_fonte(url)
    conteudos = []
    
    with resposta as r:
        items = r.html.find('item', first=False)

        for item in items:
            titulo = item.find('title', first=True).text
            data_publicacao = item.find('pubDate', first=True).text
            guid = item.find('guid', first=True).text
            descricao = item.find('description', first=True).text
            enclosure = item.find('enclosure', first=True)
            encoded = item.find('encoded', first=True).html

            from ipdb import set_trace; set_trace()
        row = {
            'title': titulo, 
            'data_publicacao': data_publicacao, 
            'guid': guid, 
            'description': descricao
        }
        conteudos.append(row)

        return conteudos