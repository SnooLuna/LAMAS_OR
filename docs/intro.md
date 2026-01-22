---
title: Introduction
---

This should have a detailed introduction section with references and everything, introduce all 3 approaches we have.

# Topic Introduction
It is well known that humans vary in the depth of Theory of Mind (Premack & Woodruff 1978) they apply when solving puzzles that require reasoning about what others know (about you). Traditional riddles often consist of a single correct answer, regardless of how deep someone reasons. This project tries to find if epistemic logic can be used to design riddles in which the final answer itself reveals the depth of Theory of Mind that was used by the person solving the riddle. Instead of having only one correct solution, the riddle is constructed so that each additional layer of epistemic reasoning corresponds to a different observable answer.
For this project we will try to construct such a riddle which showcases how many orders of Theory of Mind someone comprehends based on their final answer. This can be very useful when investigating how humans process riddles for higher theory of mind. We can formalize this in the following research question.

**Research question:** Is there a combination of Kripke model and set of announcements such that when combined into a riddle, can distinguish between the orders of Theory of Mind used by the solver by the answer they give?

We originally assume that our riddle will be able to make use of S5 and that this is also an intuitive way of thinking for people solving riddles (References for this to be added.), which is why this is the basis of our first approach. If this proves to be impossible, we will also consider riddles that make use of Kripke models that are not symmetric or transitive. We do think a desired Kripke model corresponding to our riddle should always be reflexive, since agents within the riddle are always thought of as perfect logicians. Without reflexivity, a public announcement would lose power, as agents could ‘know’ things that are factually false, breaking the logical consistency of the riddle’s solution. Therefore, we will focus on reflexive Kripke models.

In our attempt to find an answer to this research question, we will look into 3 different approaches:

*Approach 1*: 
In our first approach, we investigate whether it is possible to distinguish different orders of Theory of Mind using standard reflexive Kripke models that correspond to idealized agents with perfect logical reasoning. We try to design announcements so that each one points to exactly one possible world. If this worked, each added layer of reasoning would lead to a different answer in the riddle. However, we found that in this kind of model, it is not possible to make each announcement select a different world. This approach showed us that we had to soften or change some assumptions in our next approaches.

*Approach 2*:
Our second approach builds on the things that we learned from the first approach by allowing multiple worlds to satisfy each announcement, instead of requiring a single unique world. To still get a unique answer for the riddle, we impose a natural order on the worlds and define 'the answer' as the world with the highest order among those worlds that satisfy the announcement. This way, each layer of reasoning can correspond to a different answer, even if multiple worlds satisfy an epistemic formula. Based on this idea, we constructed a Kripke model with five worlds where different announcements each lead to a unique world. This allows us to create riddles where the solver's answer reflects the depth of Theory of Mind that they applied during solving.

*Approach 3*:
The third approach tries to automate the search for unique answers by using a solver that evaluates epistemic logic formulas with announcements on a randomly created Kripke model. The solver creates Kripke models with different worlds, relations, truth valuations and knowledge formulas using K operators. The solver works by removing the lefmost K operator from a formula and computing the set of worlds where the resulting formula is satisfied. This approach lets us test many combinations of worlds, relations and valuationss to see if any configuration/combination produces a sequence of unieuqwe answers corresponding to different levels of Theory of Mind.

.
