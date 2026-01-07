import bcrypt

def create_password(password):
    pw = password.encode()
    s = bcrypt.gensalt()
    h = bcrypt.hashpw(pw, s)
    return h

def check_password(entered_pw, password):
    pw_bytes = entered_pw.encode()
    if bcrypt.checkpw(pw_bytes, password):
        return True
    else:
        return False
