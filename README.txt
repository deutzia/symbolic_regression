So far, in science there have been three main branches: theory, experimnet and simulations. Recently, a fourth one poped up: artificial intelligence. This is the one invesigated in this project.
The aim of this project is to apply genetic algorithm called symbolic regression to some data to disvover equations that fit the data the best.
For example, the oscilator moves can be described with sin(t). We want to be able to get this equation from the data from the oscilator (how it moves).

The lgorithm has six phases:
1) getting the data
2) calculating partial deriviatives for the data
3) creating candidate functions (randomly)
4) deriving the functions and comparing with numerical deriviatives
5) selecting the best functions based on how well the deriviatives match, discard the rest
6) randomly changing the equations (crossoves, mutations)
steps 4-6 are repeated until desires accuracy is reached
It is possible that in the future scientists will be able to use this algorithm to get new equations from experimental data, even the more complicated ones.

One issue with the code is I don't know how to fix it that it tends to overcomplicate. What I mean, is that it can write simble expressions like a+b=0 in a form c*a*(a+b)**3 or something like this.
