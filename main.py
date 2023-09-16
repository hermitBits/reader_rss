from entidades.usuario import Usuario
from entidades.rss_fonte import RssFonte

from repositorios.usuario_repositorio import InMemoryRepositorioUsuario
from repositorios.rss_fonte_repositorio import InMemoryRepositorioRSSFonte

from modulos.rss.rss_core import pegar_feed

#############################################################
# USUARIO
banco = {}

repositorio_usuarios = InMemoryRepositorioUsuario(
    dictionary_structure=banco
)

primeiro_usuario = Usuario(
    nome='Mateus',
    usuario_nome='mateus',
    senha='senha'
)

salvando_usuario = repositorio_usuarios.save(usuario=primeiro_usuario)

if salvando_usuario:
    print(f'usuário criado com sucesso! - {salvando_usuario}')

#############################################################
# RSS FONTE
banco = {}

repositorio_rss_fontes = InMemoryRepositorioRSSFonte(
    dictionary_structure=banco
)

primeiro_rss_fonte = RssFonte(
    nome='Segurança Legal',
    url='https://www.segurancalegal.com/feed/'
)

salvando_rss_fonte = repositorio_rss_fontes.save(
    rss_fonte=primeiro_rss_fonte
)

if salvando_rss_fonte:
    print(f'rss fonte criado com sucesso! - {salvando_rss_fonte}')

#############################################################
# PEGANDO RSS
url = 'https://www.segurancalegal.com/feed/'
conteudos = pegar_feed(url)

if conteudos:
    for conteudo in conteudos:
        print('Titulo: {} GUID: {}'.format(
            conteudo.get('titulo'), 
            conteudo.get('guid')
        ))
