from Kripke import Model


class Solver:
    def __init__(self, formula, model: Model = None, verbose: bool = False):
        """
        Initialize the solver with a starting formula, set of worlds, relations and valuations

        To Do: Add support for NOT operator, and, or etc.

        :param formula: Description
        :param model:
        :param verbose:
        """
        self.start = formula
        self.level = 0
        self.f = formula
        self.w = model.worlds if model.worlds else model.create_worlds()
        self.r = model.relations if model.relations else model.create_relations()
        self.v = model.valuations if model.valuations else model.create_valuations()
        self.talks = verbose

    def eval_formula(self, formula, world):
        if formula[0] == "p":
            return world in self.v.get("p", set())
        if formula[0] == "K":
            agent, sub_formula = formula[1], formula[2]
            return all(self.eval_formula(sub_formula, connected_world)
                       for connected_world in self.r[agent][world])

    def satisfying_worlds(self):
        return {w for w in self.w if self.eval_formula(self.f, w)}

    def strip_outer_K(self):
        self.f = self.f[2] if self.f[0] == "K" else self.f

    def analyze(self):
        answers = []

        while True:
            ws = self.satisfying_worlds()

            # print(f"\nToM level {self.level}")
            if self.talks:
                print("\n")
                print("Formula:", self.f)
                print("Possible worlds:", ws)

            if not ws:
                if self.talks:
                    print("→ inconsistent announcement")
                answers.append(None)
            elif len(ws) == 1:
                ans = next(iter(ws))
                if self.talks:
                    print("→ unique world:", ans)
                answers.append(ans)
            else:
                p_vals = {self.eval_formula(("p",), w) for w in ws}
                if self.talks:
                    if len(p_vals) == 1:
                        print("→ p is known =", p_vals.pop())
                    else:
                        print("→ no unique outcome")
                answers.append(None)

            if self.f[0] != "K":
                break

            self.strip_outer_K()
            self.level += 1

        unique_answers = [a for a in answers if a is not None]
        if (len(unique_answers) == len(set(unique_answers))
                and len(unique_answers) == len(answers)):
            print("\nUnique different answer found for each K operator removed.")
            print("Formula:", self.start)
            print("worlds:", self.w)
            print("relations:", self.r)
            print("valuations:", self.v)
        else:
            print("\t\tNo unique different answer found for each K operator removed.")
