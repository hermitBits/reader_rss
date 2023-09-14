from entidades.usuario import Usuario
from entidades.rss_fonte import RssFonte
from entidades.relacao_usuario_fonte import RelacaoUsarioFonte

from repositorios.usuario_repositorio import InMemoryRepositorioUsuario
from repositorios.rss_fonte_repositorio import InMemoryRepositorioRSSFonte
from repositorios.relacao_usuario_fonte_repositorio import (
    InMemoryRepositorioRelacaoUsuarioFonte
)

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
# RSS FONTE e USUARIO RELACAO
banco = {}

repositorio_relacao_fonte_usuario = InMemoryRepositorioRelacaoUsuarioFonte(
    dictionary_structure=banco
)

primeira_relacao = RelacaoUsarioFonte(
    fonte_id=salvando_rss_fonte.get('id'),
    usuario_id=salvando_usuario.get('id')
)

salvando_relacao = repositorio_relacao_fonte_usuario.save(
    relacao=primeira_relacao
)

if salvando_relacao:
    print(f'relacao criada com sucesso! - {salvando_relacao}')

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
