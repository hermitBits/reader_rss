class UsuarioNomeJaExiste(Exception):
    def __init__(self, mensagem="Usuãrio com esse nome jã existe"):
        super().__init__(mensagem)

class SenhaCurta(Exception):
    def __init__(self, mensagem="Senha muito curta, menor que 5 caracteres"):
        super().__init__(mensagem)