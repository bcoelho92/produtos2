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