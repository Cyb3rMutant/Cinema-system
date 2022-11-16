import admin
import cinema


class Manager(admin.Admin):
    def __init__(self, name: str, id: int, branch: cinema.Cinema):
        super(Manager, self).__init__(name, id, branch)
