---
title: First approach
---

# First approach, unique world as answer in reflexive Kripke model
Our first and somewhat naive approach was to make some strong
assumptions on our Kripke model and try to find a model with
announcement that allows us to distinguish between different orders of
ToM as described in the introduction. However, our assumptions did prove
to be too strong and we could actually prove that no desired riddle
could exists with our assumed assumptions. Although no riddle came out
of this approach, we still wanted to include it in since it gives some
intuition into the direction of a model and assumptions that would
work.\

## Assumptions

-   **Agents:** We will assume two agents $A$ and $B$.

-   **Kripke model:** We will assume a reflexive Kripke model with a set
    of worlds $S$, a specified truth valuation $\pi$ and a relations
    $R_A$ and $R_B$.

-   **Announcements:** We fix a finite epistemic depth $n$ where $n$ is
    a natural number. We consider a sequence of public announcements
    obtained by alternately prefixing knowledge operators of agents $A$
    and $B$ to a base formula $\varphi$, up to depth $n$. That is, the
    announcements are of the form
    $$\varphi,\; K_B\varphi,\; K_AK_B\varphi,\; K_BK_AK_B\varphi,\; \ldots$$
    where the maximum nesting depth of knowledge operators is $n$.

-   **Riddle solution:** The solution to the riddle is the only world in
    which a public announcement holds, if an announcement holds in
    multiple worlds the riddle has no solution.

We then want to find a Kripke model such that every announcement
corresponds to a different unique solution. This would mean that we can
distinguish between different orders of ToM.\
We can prove that these assumptions are too strong and we cannot find a
Kripke model that satisfies our goal. We will even prove something
stronger with a contradiction. We will prove that there cannot exist two
announcements that differ by one leading knowledge operator that lead to
two unique distinct worlds. Assume that it is possible to find such a
Kripke model $M$ and announcements with a base formula $\psi$ and
alternating knowledge operators as stated in the assumptions. Then by
our assumptions there must exist two announcements that differ by one
leading knowledge operator that lead to two unique distinct worlds.
Consider a logical formula of the form $\varphi = \ldots K_B \psi$,
where the $\ldots$ represent alternating knowledge operators $K_A$ and
$K_B$. Here $\psi$ is some other logical formula. Since this world $M$
satisfies the assumptions, we know that $\varphi$ is only true in one
unique world $v_1$ and $K_A\varphi$ is only true in one unique world
$v_2$ with $v_1 \neq v_2$.\
Now by the definition of $K_A$ that for all worlds $w$ it holds that

$$(M,w) \models K_A \varphi
\quad \text{iff} \quad
\text{for all } t \in S \text{ such that } w R_A t, \text{ we have that }\; (M,t) \models \varphi$$

However, since we have already assumed that $\varphi$ is only true in
world $v_1$, we see that 
$$(M,w) \models K_A \varphi
\quad \text{iff} \quad
 w \in S \text{ such that the only $A$ relation of $w$ is } v_1$$
 
However, since we are looking at a reflexive Kripke model we know that
$v_2R_Av_2$. Since $v_2 \neq v_1$ this automatically implies that
$(M,v_2) \not\models K_A \varphi$, which is a contradiction to what we
assumed and therefore it is not possible to get two unique different
worlds as answers for two announcements that differ by one leading
knowledge operator.
