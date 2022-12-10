import cinema


class User():
    def __init__(self, name: str, id: int, branch: cinema.Cinema):

        self._name = name

        self._id = id

        self._branch = branch

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id

    def get_branch(self):
        return self._branch
