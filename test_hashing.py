from hashing import create_password, check_password

def test_create_password():
    hashed = create_password("mypassword")
    assert isinstance(hashed, bytes)

def test_check_password_success():
    password = "secure123"
    hashed = create_password(password)
    assert check_password(password, hashed) is True

def test_check_password_failure():
    hashed = create_password("secure123")
    assert check_password("wrongpassword", hashed) is False