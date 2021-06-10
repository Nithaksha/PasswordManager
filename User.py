import Credmanager


class User:

    def __init__(self, username: str, password: str):
        self.username = username.lower()
        self.password = password
        self.cipher = Credmanager.gen_cipher(username)

    def __str__(self):
        return 'Username: ' + self.username + ' Password: ' + self.password
