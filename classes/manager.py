from admin import Admin
from cinema import Cinema


class Manager(Admin):
    def __init__(self, name: str, id: int, branch: Cinema):
        super(Manager, self).__init__(name, id, branch)

    def add_cinema(self):
        pass
