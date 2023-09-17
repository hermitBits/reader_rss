import pytest

from faker import Faker

from entidades.usuario import Usuario

from repositorios.usuario_repositorio import InMemoryRepositorioUsuario

from casos_de_uso.usuario.todos_usuario import CasodeUsoTodosUsuario
from casos_de_uso.usuario.criar_usuario import CasodeUsoCriarUsuario
from casos_de_uso.usuario.criar_usuario import CriarUsuarioSolicitar
from casos_de_uso.usuario.usuario_errors import SenhaCurta, UsuarioNomeJaExiste


fake = Faker()


@pytest.fixture
def repositorio_setup():
    banco = {}

    repositorio = InMemoryRepositorioUsuario(
        dictionary_structure=banco
    )
    
    usuario_teste = Usuario(
        nome=fake.name(),
        usuario_nome='usuario123',
        senha='senha123'
    )

    repositorio.save(usuario_teste)

    yield repositorio


def test_criar_repositorio(repositorio_setup):
    assert isinstance(repositorio_setup, InMemoryRepositorioUsuario)


def test_caso_de_uso_todos_usuario(repositorio_setup):
    todos_usuarios = CasodeUsoTodosUsuario(
        repositorio=repositorio_setup
    ).execute()

    assert todos_usuarios.length == 1


def test_caso_de_uso_criar_usuario_ja_existe(repositorio_setup):
    solicitacao_criar_usuario = CriarUsuarioSolicitar(
        nome=fake.profile().get('name'),
        usuario_nome='usuario123',
        senha='senha123'
    )

    with pytest.raises(UsuarioNomeJaExiste):
        CasodeUsoCriarUsuario(
            repositorio=repositorio_setup
        ).execute(
            solicitar=solicitacao_criar_usuario
        )


def test_caso_de_uso_criar_usuario_senha_curta(repositorio_setup):
    solicitacao_criar_usuario = CriarUsuarioSolicitar(
        nome=fake.profile().get('name'),
        usuario_nome=fake.profile().get('username'),
        senha='s'
    )

    with pytest.raises(SenhaCurta):
        CasodeUsoCriarUsuario(
            repositorio=repositorio_setup
        ).execute(
            solicitar=solicitacao_criar_usuario
        )


def test_caso_de_uso_criar_usuario(repositorio_setup):
    solicitacao_criar_usuario = CriarUsuarioSolicitar(
        nome=fake.profile().get('name'),
        usuario_nome=fake.profile().get('username'),
        senha=fake.password(length=12)
    )

    usuario = CasodeUsoCriarUsuario(
        repositorio=repositorio_setup
    ).execute(
        solicitar=solicitacao_criar_usuario
    )

    assert isinstance(usuario, Usuario)
