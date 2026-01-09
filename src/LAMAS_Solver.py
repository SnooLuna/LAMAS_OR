def eval_formula(f, w, R, valuation):
    if f[0] == "p":
        return w in valuation.get("p", set())
    if f[0] == "K":
        agent, sub = f[1], f[2]
        return all(eval_formula(sub, v, R, valuation) for v in R[agent][w])


def satisfying_worlds(formula, worlds, R, valuation):
    return {w for w in worlds if eval_formula(formula, w, R, valuation)}


def strip_outer_K(formula):
    return formula[2] if formula[0] == "K" else formula


def analyze(formula, worlds, R, valuation):
    level = 0
    current = formula
    answers = []

    while True:
        ws = satisfying_worlds(current, worlds, R, valuation)

        # print(f"\nToM level {level}")
        print("\n")
        print("Formula:", current)
        print("Possible worlds:", ws)

        if not ws:
            print("→ inconsistent announcement")
            answers.append(None)
        elif len(ws) == 1:
            ans = next(iter(ws))
            print("→ unique world:", ans)
            answers.append(ans)
        else:
            p_vals = {eval_formula(("p",), w, R, valuation) for w in ws}
            if len(p_vals) == 1:
                print("→ p is known =", p_vals.pop())
            else:
                print("→ no unique outcome")
            answers.append(None)

        if current[0] != "K":
            break

        current = strip_outer_K(current)
        level += 1

    unique_answers = [a for a in answers if a is not None]
    if (len(unique_answers) == len(set(unique_answers))
            and len(unique_answers) == len(answers)):
        print("\nUnique different answer found for each K operator removed.")
    else:
        print("\nNo unique different answer found for each K operator removed.")


# INPUT (will later be moved outside of this code so you can input it yourself, but for now this is an example of input you can give to run it)

worlds = ["w1", "w2", "w3", "w4"]

R = {
    "A": {
        "w1": {"w1"},
        "w2": {"w2"},
        "w3": {"w3"},
        "w4": {"w4"},
    },
    "B": {
        "w1": {"w1", "w2"},
        "w2": {"w2", "w3"},
        "w3": {"w1"},
        "w4": {"w1"},
    }
}

valuation = {
    "p": {"w1", "w2", "w3"}
}

formula = ("K", "A", ("K", "B", ("K", "A", ("K", "B", ("p",)))))

analyze(formula, worlds, R, valuation)
