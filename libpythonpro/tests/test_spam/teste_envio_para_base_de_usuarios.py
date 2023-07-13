from unittest.mock import Mock

import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Pedro', email='pedro25mascarenhas@gmail.com'),
            Usuario(nome='Luciano', email='pedro25mascarenhas@gmail.com')
        ],
        [
            Usuario(nome='Pedro', email='pedro25mascarenhas@gmail.com')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'pedro25mascarenhas@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Pedro', email='pedro25mascarenhas@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'luciano25mascarenhas@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    enviador.enviar.assert_called_once_with(
        'luciano25mascarenhas@gmail.com',
        'pedro25mascarenhas@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
