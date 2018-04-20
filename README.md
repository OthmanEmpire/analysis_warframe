Analysis Warframe: How Many More Runs Until It Drops?!
------------------------------------------------------
Of the data I found across three warframe posts (see below for the reference
to the original posts), the likelihood to obtain all blueprints for the
following warframes are:


A Bit About The Graphs
----------------------
The graphs are obtained through numerical means so there is some small error
between them and reality but nothing significant. Crudely speaking, each graph
simulates 50 consecutive boss runs and repeats this process 100,000 times to
arrive at a better average of the probabilities (so a total of 5,000,000 runs).

The real point of interest is the cumulative probability (green line) as
opposed to the probability (red line). The cumulative probability (green line)
gives the probability of obtaining all Warframe parts during any of the
consecutive runs. On the other hand, the probability (red line) gives the
probability of obtaining all Warframe parts in exactly some specified runs.
So for instance looking at Nyx's graph, we have a ~0.05 chance of all Nyx parts
dropping after exactly 10 runs but we have a ~0.80 chance of getting all Nyx
parts in any of the runs leading up to the 10th run.


Validty of Model
----------------
As for the correctness of the model, I calculated the theoretical values of
some data points which fit in well with the graphs. Also, the calculated drop
chances of each item after running the consecutive runs simulation only differs
by a fraction from the theoretical values (which are the ones displayed in the
legend of the graphs). So it seems to be fine.


Rhino Warframe Drop Chance
![](plot_rhino.png)
If attempting 9 runs, you have a ~90% chance of obtaining all parts of Rhino.

Excalibur Warframe Drop Chance
![](plot_excalibur.png)
If attempting 11 runs, you have a ~90% chance of obtaining all parts of Excalibur.

Nyx Warframe Drop Chance
![](plot_nyx.png)
If attempting 13 runs, then you have a ~90% chance of obtaining all parts of Nyx.

Atlas Warframe Drop Chance
![](plot_nyx.png)
If attempting 10 runs, then you have a ~90% chance of obtaining all parts of Atlas.

Some Unfortunate Warframe Drop Chance
![](plot_unfortunate.png)
If attempting 29 runs, then you have a ~90% chance of obtaining this all parts of this unfortunate Warframe.


Misconceptions
--------------
Question: Does that mean after I do 11 runs of Excalibur, that my chances of
getting the last piece (say item 'c') is roughly above 90% on the 12th and
subsequent runs?

Answer: No, that isn't true, that is known as the Gambler's Fallacy. For the
12th run, your probability of obtaining the last item (item 'c') will still
40% as always.

If you have completed 11 runs and not all your Warframe parts have dropped,
then the next subsequent run will not have an above 90% drop chance. But, if
you start a new second series of 11 runs from this point, then over the span of
those runs, you have a chance at least greater than ~90% of obtaining all parts
(it's actually ~99.7%). The second series of 11 runs have a higher probability
than the first series of 11 runs because they assume you already have 2/3 pieces
within possession. And now suppose after completing the second series of runs
(so a total of 22 runs so far), the last piece didn't drop unfortunately. Then,
if you complete a third series of 11 runs, you would still have a ~99.7% chance
of getting the last piece (with a total of 33 runs).

This probability differs from if you initially attempted to complete a series
of 33 runs without 'stopping' (which is ~99.9%). Why? Because in the case of
where we 'stopped', the probability of obtaining all the parts didn't proc in
the first nor second series of 11 runs. So we only had 11 more tries as oppose
to 33 hence the probability being less (even though we had 2/3 items already
which increased it).

On a side note, the probability mentioned in the question is cumulative so that
implies when looking at the corresponding runs, they essentially mean from any
number of runs less than or equal to the run.


Author
-------
Othman Alikhan, oz.alikhan@gmail.com


Credits
--------
- Nyx: https://forums.warframe.com/index.php?/topic/195825-thank-you-phorid/#entry2276005
- Rhino: https://forums.warframe.com/index.php?/topic/206582-warframe-part-drop-rates-experiments/
- Excalibur: https://forums.warframe.com/index.php?/topic/119448-drop-proportions-of-warfarme-blueprints/
