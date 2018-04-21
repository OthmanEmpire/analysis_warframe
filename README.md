Analysis Warframe: How Many More Runs Until It Drops?!
------------------------------------------------------
The aim of this project is to examine the drop chances of blueprints from bosses
with a particular emphasis on the following question: 'How many more runs
until I get all my blueprints?!'.

We examine the following warframes: Rhino, Excalibur, Nyx, and Atlas (if you
wish to see the behaviour of another warframe, feel free to email me).
Though this project examines loot drop chances for warframes in particular, it
is applicable to any other game with drop chances.


A Bit About The Plots
---------------------
In all the plots, the green line is the probability of obtaining all warframe
parts after X runs or less. This a cumulative probability plot and our main
focus. The red line on the other hand is the probability of obtaining all the
warframe parts after X runs exactly.

So for instance looking at Rhino's plot below (first plot), we have a ~0.02
chance of all Rhino parts dropping after exactly 10 runs (red line). However,
we have a ~0.91 chance of getting all Rhino parts in any of the runs leading
up to the 10th run (green line).


Validty of Simulation
---------------------
The graphs are obtained through numerical means rather than exact computation
hence introducing some error though insignificant in this case. Crudely
speaking, each plot below simulates 50 consecutive boss runs and repeats this
process 100,000 times to average the probabilities, thus reducing errors
stemming for numerical computation.

As for the correctness of the model, we stored the amount of times each item
was dropped during the simulation. We then calculated the drop chance of each
item purely from this data and the results were no more than 5% from the
input probabilities fed into the simulation, thus confirming that simulation is
functioning correctly. The input probabilities were obtained from the warframe
wikia (see Credits section).


### Rhino Warframe Drop Chance (2018-04-21)
If attempting 10 runs, you have a ~90% chance of obtaining all parts (see below).
![](plot_rhino_(2018-04-21).png)

### Excalibur Warframe Drop Chance (2018-04-21)
If attempting 10 runs, you have a ~90% chance of obtaining all parts (see below).
![](plot_excalibur_(2018-04-21).png)

### Nyx Warframe Drop Chance (2018-04-21)
If attempting 10 runs, you have a ~90% chance of obtaining all parts (see below).
![](plot_nyx_(2018-04-21).png)

### Atlas Warframe Drop Chance (2018-04-21)
If attempting 10 runs, you have a ~90% chance of obtaining all parts (see below).
![](plot_atlas_(2018-04-21).png)

### Some Unfortunate Warframe Drop Chance (2018-04-21)
If attempting 29 runs, you have a ~90% chance of obtaining all parts of this
unfortunate Warframe (see below).
![](plot_unfortunate_(2018-04-21).png)


Misconceptions
--------------
**Question:** Since the probability of obtaining all parts of Atlas on the 10th
and 11th run is roughly 90%, does this mean if I didn't obtain all parts on my
10th run, then my next run (11th run) has a probability of 90% of obtaining all
parts?

**Answer:** No, that is false. This is known as the Gambler's Fallacy. For the
11th run, your probability of obtaining the last item (item 'c') will not be 90%
but equal to the probability of that item dropping in exactly one instance run
(in this case 22.6%).

Now, if you have completed 10 runs and not all parts have dropped, then the next
run will not have a 90% drop chance. But, if you start a new series of 10 runs
from this point, then over the span of those 10 runs, you have a 90% chance of
obtaining all parts. Actually, the new series of 10 runs will have a higher
probability than the first series of 10 runs because you already have 2 out of
3 pieces.


Author
-------
Othman Alikhan, oz.alikhan@gmail.com


Credits
--------
- Rhino probabilities: http://warframe.wikia.com/wiki/Nyx
- Excalibur probabilities: http://warframe.wikia.com/wiki/Excalibur
- Nyx probabilities: http://warframe.wikia.com/wiki/Nyx
- Atlas probabilities: http://warframe.wikia.com/wiki/Atlas
