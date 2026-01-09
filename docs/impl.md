---
title: Implementation
---

# Description of the Solver

The solver that we are creating evaluates epistemic logic formulas with announcements on a given Kripke model. In the final version we want to give the user the option to input their own combinations of worlds, relations, propositional valuations and knowledge using the K operators. The solver removes the leftmost k operator from the formula in each iteration, after which it computes the set of worlds where the formula is satisfied. After processing all the subformulas, the solver checks if each level has a unique different world. If this is the case, it will report that a unique different solution was found for multiple removed k operators. Otherwise it will report that removal of K operators from the left of the formula did not lead to unique different answers.

The main idea of the solver is to test whether removing knowledge operators from the left can ever give a sequence of unique different answers/outcomes. We want to do this by running the solver on a large amount of different worlds/relations/valutions automatically to find out if we ever get unique different answers.


[Link to solver's directory](https://github.com/SnooLuna/LAMAS/tree/main/src)
