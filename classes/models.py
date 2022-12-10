from dbfunc import conn
from passlib.hash import sha256_crypt
from user_factory import User_factory
from city_container import cities


class Model():

    def validate_login(self, username, password):
        data = conn.select(
            "SELECT * FROM users u \
                LEFT JOIN cinemas c ON c.CINEMA_ID=u.CINEMA_ID \
                    WHERE USER_NAME=%s", username)

        if (data):
            data = data[0]
            hash = data["USER_PASSWORD_HASH"]
        else:
            return -1

        if (sha256_crypt.verify(password, hash)):
            cinema = cities[data["CITY_NAME"]][data["CINEMA_ID"]]

            user = User_factory.get_user_type(data["USER_TYPE"])(
                data["USER_NAME"], data["USER_ID"], cinema)

            return user
        else:
            return 0
