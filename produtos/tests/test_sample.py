"""
Test é formado por 3 etapas - TDD

- givem - dado 
- when - quando
- then - então

Outra abordagem 3-A

- Arange
- Act
- Assert

Comandos para rodar pytest

- pytest -v / mostra o nome dos tests executados e seus status
- pytest -x / roda os testes e para no que quebrar
- pytest -k "email" / executar o(s) test(s) por um kname especifico ex: "email"
- pytest -v -k "email" / variação
- pytest -s / mostra as saidas no console - Print("cheguei aqui")
- pytest --pdb / debugar quando falha 
- python3 -m pytest 


- pytest --junitxml report.xml / salva o report dos tests 
- pytest -v --junitxml report.xml / variação

MARK / marcações ou argumentos, metadados 

from pytest import mark

@mark.tag
def test_exemplo_testando():
    pass

Marcar testes que testam coisas especificas / "usuario" 

- pytest -m usuario / Rodar teste marcado @mark
- pytest -m "not usuario" / Rodar teste que nao tem o mark "usuario"

Parametrize - utilizar varias entradas para um mesmo test 

- @mark.parametrize(
-     'name_user,email',
-     [("Carlos","Carlos1@hotmail"),("Carlos","Carlos1.hotmail")]
- )
- @mark.usuario
- def test_user_create_validavao_email_unico(name_user, email):
-     pass

"""
from pytest import mark

@mark.usuario
def test_user_create_correto():
    pass

@mark.parametrize(
    'name_user,email',
    [("Carlos","Carlos1@hotmail"),("Carlos","Carlos1@hotmail")]
)
@mark.usuario
def test_user_create_validavao_email_unico():
    pass

@mark.delete
def test_user_delete():
    pass