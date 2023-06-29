import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['foo@bar.com.br', 'pedro.mascarenhas@ufba.br']
)
def test_remetente(destinatario):
    enviador = Enviador()

    resultado = enviador.enviar(
        destinatario,
        'pedro25mascarenhas@gmail.com',
        'Cursos Python Pro',
        'Primeira turma Guido Von Rossum aberta'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'pedro']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'pedro25mascarenhas@gmail.com',
            'Cursos Python Pro',
            'Primeira turma Guido Von Rossum aberta'
        )
