from dbfunc import conn
from passlib.hash import sha256_crypt


class Model():
    def validate_login(self, username, password):
        data = conn.select(
            "SELECT * FROM users WHERE USER_NAME=%s", username)

        if (data):
            hash = data[0]["USER_PASSWORD_HASH"]
        else:
            return -1

        if (sha256_crypt.verify(password, hash)):
            return data[0]
        else:
            return 0
