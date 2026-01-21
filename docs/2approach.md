---
title: Second approach
---

# Second approach, multiple worlds, unique answer
  
Based on our findings during our first approach we concluded that we should focus on Kripke models/ riddles where the answer of the riddle is not a unique world. The most natural way to get rid of this is by imposing a natural order on the worlds, such that when there are multiple worlds that satisfy some announcement $K_BK_A \ldots K_B \psi$ the answer to the riddle is then found by finding all worlds that satisfy this announcement and picking the world out of the possible worlds that comes first in the imposed order. This will result in a unique world as answer and we could potentially construct a Kripke model such that every layer corresponds to a different answer. Although this problem is still not trivial, we were able to construct a Kripke model that satisfies the condition that every layer results in a different answer.
  
## Description of the Kripke model
  
Consider a Kripke model with 5 states. $S = \{w_1, w_2, w_3, w_4, w_5\}$. The truth valuation is the following; $\pi'(p) = S \setminus \{w_5\}$, so $p$ is true in all worlds except world $w_5$. Then there are two types of relations $R$, namely relations for agent $A$, $R_A$ and relations for agent $B$, $R_B$. We have $$R_A = \{(w_1,w_1),(w_2,w_2), (w_3,w_3), (w_4,w_4), (w_5,w_5), (w_2,w_3), (w_3,w_2), (w_4,w_5), (w_5,w_4)\}$$and $$R_B = \{(w_1,w_1),(w_2,w_2), (w_3,w_3), (w_4,w_4), (w_5,w_5), (w_1,w_2), (w_2,w_1), (w_3,w_4), (w_4,w_3)\}$$the model can be found in Figure 1.

![Model](/assets/img/model.png)
  
## Natural order and announcements
  
Now we assume the natural order $w_5 \geq w_4 \geq w_3 \geq w_2 \geq w_1$. This means that the answer to the riddle with announcement $\phi$ is given by the world with the highest order among all worlds that satisfy the announcement $\phi$. For the announcements we consider $p$, $K_Ap$, $K_BK_Ap$, $K_AK_BK_Ap$.
  
## Solving for every layer
  
The problem we now have to solve is the following, for every announcement, which world that satisfies this announcement has the highest order. We will show that every different announcement will result in a different answer.
  
### $p$:
  
For $p$ this is easy, we have that $p$ is true in all worlds except for world $w_5$. This means that $p$ is true in worlds $\{w_1,w_2,w_3,w_4\}$. Since for these four worlds $w_4$ has the highest order the answer to this announcement will be world $w_4$
  
### $K_Ap$:
  
We have that in a certain world $K_Ap$ holds when $p$ holds in all worlds $A$ connected to that given world. Since $p$ does hold in all worlds except for world $w_5$, we have that $K_Ap$ holds in all worlds that do not have an $A$ relation with world $w_5$. This is true for worlds $w_1$, $w_2$ and $w_3$ since worlds are only possibly connected to neighbouring worlds. However, world $w_4$ is $A$ connected with world $w_5$ and therefore $K_Ap$ is not true in world $w_4$. It is also not true in world $w_5$ since this world is $A$ connected with itself. This means that $K_Ap$ is only true in worlds $\{w_1, w_2, w_3\}$ and the answer to this announcement is $w_3$ since this world has the highest order.
  
### $K_BK_Ap$:
  
We have that in a certain world $K_BK_Ap$ holds when $K_Ap$ holds in all worlds $B$ connected to that given world. Since $K_Ap$ does hold in all worlds except for world $w_4$ and $w_5$, we have that $K_BK_Ap$ holds in all worlds that do not have a $B$ relation with world $w_4$ or world $w_5$. This is true for worlds $w_1$ and $w_2$ since worlds are only possibly connected to neighbouring worlds. However, world $w_3$ is $B$ connected with world $w_4$ and therefore $K_BK_Ap$ is not true in world $w_3$. It is also not true in worlds $w_4$ and $w_5$ since these worlds are all $B$ connected with themselves. This means that $K_BK_Ap$ is only true in worlds $\{w_1, w_2\}$ and the only remaining state after this announcement is $w_2$ since this world has the highest order.
  
### $K_AK_BK_Ap$:
  
We have that in a certain world $K_AK_BK_Ap$ holds when $K_BK_Ap$ holds in all worlds $A$ connected to that given world. Since $K_BK_Ap$ does hold in all worlds except for world $w_3, w_4$ and $w_5$, we have that $K_AK_BK_Ap$ holds in all worlds that do not have a $A$ relation with world $w_3, w_4$ or $w_5$. This is true for world $w_1$ since worlds are only possibly connected to neighbouring worlds. However, world $w_2$ is $A$ connected with world $w_3$ and therefore $K_AK_BK_Ap$ is not true in world $w_2$. It is also not true in worlds $w_3, w_4$ and $w_5$ since these worlds are all $A$ connected with themselves. This means that $K_AK_BK_Ap$ is only true in world $\{w_1\}$ and the only remaining state after this announcement is $w_1$ since this world has the highest order. 
  
![Model](/assets/img/model.png)
  
Figure 1: Described Kripke model.

 
## From Kripke model to riddle

 
It is pretty easy to transform the Kripke model to a riddle once we have found the suitable model. In our case we have chosen a cookies in a jar riddle. Here world $w_i$ corresponds to a jar with $i$ cookies. Here we present the riddle that corresponds with the announcement $K_BK_Ap$. In this riddle, Alex and Bob are perfect logicians who never lie, and this is common knowledge among both. The riddle has a relation with the consecutive numbers riddle [who to cite here?]

**Given a jar with cookies. Alex and Bob both took one cookie from the jar, which is something they both know, but they don't know in what order they went for a cookie. After Alex took a cookie from the jar she saw an odd number of cookies. After Bob took a cookie from the jar he saw an even number of cookies. Given that Bob knows that Alex knows that there are less than 5 cookies in the jar, how many cookies are maximally in the jar?**

This riddle does not account for the fact that Bob could also have seen 5 cookies according to the Kripke Model and that for Alex there could be 0 cookies in the jar, so maybe we should modify or Kripke model to an infinite line?

This riddle can be solved by reasoning in the following way. If Bob knows that Alex knows that there are less than 5 cookies in the jar, he must know for certain that Alex saw 1 or 3 cookies when Alex looked inside the jar. This means that when Bob looked inside the jar there could not have been 4 cookies since then Alex could potentially have seen 5 cookies. This means that there could maximally be 2 cookies in the jar when Bob looked inside the jar and therefore the maximum number of cookies inside the jar is 2. Note that this riddle can be extended to any level of ToM that is satisfactory by just increasing the number of cookies.
  
# Other ideas
  
Most of the other ideas focus on finding a solution such that every layer corresponds to a unique world. This could be done by changing the layers or changing the Kripke model.
  
-   Maybe it is possible with unique worlds as answers when we focus on $K_B\phi$, $K_BK_AK_B\phi$ and $K_BK_AK_BK_AK_B\phi$ or $K_B\phi$, $K_BK_A\phi$ and $K_BK_AK_B\phi$
  
-   We could also use $\neg K$ instead of $K$, maybe that changes things
  
-   What about three agents $A$, $B$ and $C$? Could we then also construct these layers?
  
-   What about non reflexive Kripke models, it should be possible to construct a Kripke world such that every layer corresponds with a unique world, but is it possible to construct a riddle from such a model?
