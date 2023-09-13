from uuid import UUID


class RssConteudo:
    id: UUID
    id_fonte: UUID
    titulo: str
    data_publicacao: str
    guid: str
    descricao: str
    media: str
    conteudo: str
