---
title: First approach
---

# First approach: impossibility of unique-world solutions in reflexive Kripke models
In our first approach we made some strong
assumptions on our Kripke model and searched for a model with
announcement that allows us to distinguish between different orders of
ToM as described in the introduction. We imposed these strong structural assumptions on the Kripke model, in order to test whether distinguishing different orders of Theory of Mind is even possible under idealized conditions. However, our assumptions are too strong and no desired riddle
could exists under these assumptions. Although no riddle came out
of this approach, we still wanted to include it in since it gives some
intuition into the direction of a model and assumptions that would
work.

## Assumptions

-   **Agents:** We will assume two agents $a$ and $b$.

-   **Kripke model:** We will assume a reflexive Kripke model with a set
    of worlds $S$, a specified truth valuation $\pi$ and a relations
    $R_a$ and $R_b$. Reflexivity is assumed to model agents having correct introspective access to their own knowledge, which is also the standard assumption when transforming riddles into a Kripke model.

-   **Announcements:** We fix a finite depth $n$ where $n$ is
    a natural number. Here we define the depth as the maximum number of nested knowledge operators occurring in it. We consider a sequence of public announcements
    obtained by alternately prefixing knowledge operators of agents $a$
    and $b$ to a base formula $\varphi$, up to depth $n$. That is, the
    announcements are of the form
    $$\varphi,\; K_b\varphi,\; K_aK_b\varphi,\; K_bK_aK_b\varphi,\; \ldots$$
    where the maximum nesting depth of knowledge operators is $n$.

-   **Riddle solution:** A solution to the riddle is defined as a unique world in which a given public announcement holds. If a public announcement is true in more than one world, the riddle is considered unsolved.

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
Consider a logical formula of the form $\varphi = \ldots K_b \psi$,
where the $\ldots$ represent alternating knowledge operators $K_a$ and
$K_b$. Here $\psi$ is some other logical formula. Since this world $M$
satisfies the assumptions, we know that $\varphi$ is only true in one
unique world $v_1$. We extend $\varphi$ with one knowledge operator to obtain $K_A\varphi$ (or $K_B\varphi$ but the argument will work the same). By our assumptions $K_A\varphi$ is only true in one unique world $v_2$ with $v_1 \neq v_2$.
Now by the definition of $K$ that it holds for all worlds $w$ that

$$(M,w) \models K_a \varphi
\quad \text{iff} \quad
\text{for all } t \in S \text{ such that } w R_a t, \text{ we have }\; (M,t) \models \varphi$$

However, since we have already assumed that $\varphi$ is only true in
world $v_1$, we see that 

$$(M,w) \models K_a \varphi
\quad \text{iff} \quad
 w \in S \text{ such that the only $a$ relation of $w$ is } v_1$$
 
However, since we are looking at a reflexive Kripke model we know that $v_2R_av_2$. Since $v_2 \neq v_1$ this automatically implies that $(M,v_2) \not\models K_a \varphi$. This contradicts our assumption that $(M,v_2) \models K_a \varphi$. Therefore, it is not possible to obtain two distinct unique worlds as answers for two announcements that differ by one leading knowledge operator. While we have formulated the argument for two agents $a$ and $b$, the reasoning does not depend on this choice. The proof generalizes directly to Kripke models with an arbitrary finite number of agents.
