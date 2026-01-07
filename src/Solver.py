from Kmodel import KripkeModel

class Solver():
    def __init__(self, model: KripkeModel, announcements: list(Announcements)):
        self.model = model
        self.announcements = announcements

    def solve(self):
        pass
        # does a little solving