from numpy.random import randint


# idk if random generation is the right idea,
# maybe a more systematic approach would be better.
# just trying things out for now.
class Model():
    def __init__(self, worlds=None, agents=None,
                 relations=None, valuations=None):
        self.worlds = worlds
        self.agents = agents
        self.relations = relations
        self.valuations = valuations
        if self.valuations is None:
            self.create_valuations()
        if self.relations is None:
            self.create_relations()
        if self.agents is None:
            self.create_agents()
        if self.worlds is None:
            self.create_worlds()

    def create_worlds(self, max: int = 12):
        # generate a random number of worlds
        self.worlds = []
        for i in range(randint(1, max + 1)):
            self.worlds.append(f"w{i}")
        return self.worlds

    def create_agents(self, max: int = 12):
        # generate a random number of agents
        self.agents = []
        for i in range(randint(1, max + 1)):
            self.agents.append(chr(ord('A')+i))
        return self.agents

    def create_relations(self):
        # generate random relations
        if self.worlds is None:
            self.create_worlds()
        if self.agents is None:
            self.create_agents()
        # This should make S5 models, doesn't do that yet
        self.relations = {}
        for a in self.agents:
            self.relations[a] = {}
            for world in self.worlds:
                self.relations[a][world] = {w for w in self.worlds
                                            if w == world
                                            or randint(0, 10) < 5}
        return self.relations

    def create_valuations(self, max: int = 3):
        # generate random valuations
        if self.worlds is None:
            self.create_worlds()

        atoms = [chr(ord('p')+i) for i in range(randint(1, max + 1))]
        self.valuations = {}
        for atom in atoms:
            self.valuations[atom] = {w for w in self.worlds
                                     if randint(0, 10) < 5}
        return self.valuations
