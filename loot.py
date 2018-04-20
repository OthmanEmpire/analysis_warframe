"""
Calculates the cumulative probability of obtaining all n items from a
a boss after some k runs. We assume that each item has an equal chance
of dropping. We resort to numerical estimations in doing so.
"""


__author__ = "Othman Alikhan"
__email__ = "oz.alikhan@gmail.com"


import string
import numpy as np
import matplotlib.pyplot as plt


class Item:
    """
    Representation of an in-game item that can be dropped.
    """
    itemsGenerated = 0

    def __init__(self, probability, isWanted):
        """
        Assigns an alphabet ID to the item generated and initializes.

        :param probability: Number, the probability of the item being dropped.
        :param isWanted: Boolean, whether this item is sought by the user.
        """
        self.id = string.ascii_uppercase[Item.itemsGenerated]
        Item.itemsGenerated += 1

        self.probability = probability
        self.isWanted = isWanted

        self.hasDroppedRecently = False     # Flag used to simplify code
        self.totalDrops = 0
        self.totalAttempts = 0


class Instance:
    """
    Representation of an in-game instance which drops items.
    """

    def __init__(self, itemsList):
        """
        Constructs the instance. Extracts the total amount of wanted items
        to be dropped. Also, extracts the probabilities for each item to be
        dropped.

        :param itemsList: List, containing Item objects.
        """
        self.runNum = 1
        self.totalAttempts = 0
        self.totalWantedItems = 0
        self.droppedWantedItems = 0

        self.itemsList = itemsList
        self.itemsProbabilityList = []
        for item in itemsList:
            self.itemsProbabilityList.append(item.probability)

            if item.isWanted:
                self.totalWantedItems += 1

    def plotSimulationProbabilities(self, maxRuns, iterations=10000):
        """
        Plots the probability and cumulative probability of successfully getting
        all items from the boss against the number of runs on a 2D graph using
        matplotlib.

        :param maxRuns: Number, the maximum number of instance runs.
        :param iterations: Number, used to reduce numerical errors.
        """
        title = "Number of Drops From Boss={}" \
                "\nNumber of Numerical Iterations={}" \
            .format(len(self.itemsList), iterations)
        fileName = "Items={}_Iterations={}"\
            .format(len(self.itemsList), iterations)

        # Initializing the y-axis tick marks
        yticksList = []
        for i in range(11):
            yticksList.append(i/10)

        # Generating the data
        runList, runsProbabilityList, runsCumulativeProbabilityList = \
            self.generateData(maxRuns, iterations)

        # Plotting the data
        fig = plt.figure()
        fig.canvas.set_window_title(fileName)
        fig.set_size_inches(10, 8)
        subplot = fig.add_subplot(111)

        plt.plot(runList,
                 runsProbabilityList,
                 color="r",
                 marker="x",
                 label="Probability For All Wanted Items In X Runs Exactly")

        plt.plot(runList,
                 runsCumulativeProbabilityList,
                 color="g",
                 marker="x",
                 label="Probability For All Wanted Items In X Runs or Less")

        # Shrinking graph to allow extra information to be placed on the it's
        # right (items and their drop chances)
        box = subplot.get_position()
        subplot.set_position([box.x0, box.y0, 0.8*box.width, box.height])

        for i, item in enumerate(self.itemsList):
            plt.figtext(0.80, 0.84 - i/15,
                        "Item {}: {:<3.1f}%\nWanted={}"
                        .format(item.id, 100*item.probability, item.isWanted),
                        bbox=dict(facecolor="white", alpha=0.5),
                        fontweight='bold',
                        fontsize=12)

        # Painting the columns on the right hand side below the legend
        # that contains the probability tables
        columns = list(zip(runList, runsCumulativeProbabilityList))
        leftColumn = columns[:len(runList)//2]
        rightColumn = columns[len(runList)//2:]

        plt.figtext(0.76, 0.62,
                    "Probability For All Wanted\nItems in X Runs or Less",
                    weight='bold')

        for i, (run, probability) in enumerate(leftColumn):
            plt.figtext(0.76, 0.59 - i/50,
                        "{:<2}, {:.1%}".format(run, probability))
        for i, (run, probability) in enumerate(rightColumn):
            plt.figtext(0.88, 0.59 - i/50,
                        "{:<2}, {:.1%}".format(run, probability))

        # Adjusting graph settings
        plt.title(title, fontweight="bold")
        plt.legend(loc='upper right', fontsize=12)
        plt.ylabel('Probability')
        plt.yticks(yticksList)
        plt.ylim(plt.ylim()[0], 1.2)
        plt.xlabel('Instance Runs')

        plt.show()

    def generateData(self, maxRuns, iterations=10000):
        """
        Executes the consecutive runs simulation, obtains data, calculates
        probabilities for each set of successful consecutive runs, then returns
        the processed data ready to be plotted.

        :param maxRuns: Number, the maximum number of instance runs.
        :param iterations: Number, used to reduce numerical errors.
        :return: Dictionary, mapping runs to dropped items.
        """
        runsDroppedDict = self.simulateConsecutiveRuns(maxRuns, iterations)
        return self.calculateSimulationProbabilities(runsDroppedDict)

    def simulateConsecutiveRuns(self, maxRuns, iterations=10000):
        """
        Per iteration, generates a consecutive sequence of runs until the upper
        limit is reached or until all the items have dropped in the sequence.

        Returns a dictionary that contains items of form (runNumber : Number
        of times successfully obtained all wanted items)

        :param maxRuns: Number, the maximum number of instance runs.
        :param iterations: Number, used to reduce numerical errors.
        :return: Dictionary, mapping runs to dropped items.
        """

        runsDroppedDict = {i:0 for i in range(1, maxRuns+1)}

        # Generating Data:
        # The inner while-loop represents items dropping in consecutive runs up
        # to a maximum of maxRuns runs. The outer-loop is solely to repeat this
        # process multiple times for a better numerical solution.
        for _ in range(iterations):
            # Initialization per new series of runs
            self.reset()

            while(self.runNum <= maxRuns):
                self.dropItem()

                # Checks if all items have dropped yet
                if self.haveAllItemsDropped():
                    runsDroppedDict[self.runNum] += 1
                    break

                self.runNum += 1

        return runsDroppedDict

    def calculateSimulationProbabilities(self, runsDroppedDict):
        """
        Calculates the probabilities from the data generated by the
        simulation function. The runs, probabilities and cumulative
        probabilities are calculated.

        :param runsDroppedDict: Dictionary, mapping runs to dropped items.
        """
        dimension = len(runsDroppedDict)

        runsList = dimension*[0]
        runsProbabilityList = dimension*[0]
        runsCumulativeProbabilityList = dimension*[0]

        # Calculating Data:
        # The probabilities of successful runs
        print("\nProbabilities:")
        for i, (run, drops) in enumerate(runsDroppedDict.items()):
            runsList[i] = run
            runsProbabilityList[i] = drops / self.totalAttempts
            print("Runs: {:<3} {:<3} Probability: {:<3.4f}"
                  .format(run, "||", runsProbabilityList[i]))

        # The cumulative probabilities of successful runs
        runsCumulativeProbabilityList =\
            self.calculateCumulativeProbabilities(runsProbabilityList)
        print("\nCumulative Probabilities:")
        for i, _ in enumerate(runsCumulativeProbabilityList):
            print("Runs: {:<3} {:<3} Cumulative Probability: {:<3.4f}"
                  .format(runsList[i], "||", runsCumulativeProbabilityList[i]))

        # The estimated drop chance of each item
        print("\nItem Drop Chances From Simulation Data:")
        for item in self.itemsList:
            print("Item '{}' drop chance in sample: {:.4f}"
                  .format(item.id, item.totalDrops/item.totalAttempts))

        return runsList, runsProbabilityList, runsCumulativeProbabilityList

    def dropItem(self):
        """
        Selects an item to drop based on weighted probabilities and updates
        the instance correspondingly.
        """
        itemChosen = np.random.choice(self.itemsList,
                                      p=self.itemsProbabilityList)

        # Updates by checking if the item is wanted and has dropped before
        if(itemChosen.hasDroppedRecently is False):
            itemChosen.hasDroppedRecently = True
            if(itemChosen.isWanted):
                self.droppedWantedItems += 1

        # Updates by incrementing the drop variables of the item objects
        itemChosen.totalDrops += 1
        for item in self.itemsList:
            item.totalAttempts += 1

    def haveAllItemsDropped(self):
        """
        Checks whether all wanted items have dropped from the instance.

        :return: Boolean, whether all items have dropped.
        """
        if self.droppedWantedItems == self.totalWantedItems:
            return True
        else:
            return False

    def reset(self):
        """
        Resets the instance to allow a new set of consecutive runs.
        """
        self.totalAttempts += 1

        self.runNum = 1
        self.droppedWantedItems = 0
        for item in self.itemsList:
            item.hasDroppedRecently = False

    def calculateCumulativeProbabilities(self, probabilityList):
        """
        Calculates and returns the cumulative probabilities list when given a
        probability list.

        :param probabilityList: List, containing probabilities.
        """
        cumulativeProbability = 0
        cumulativeProbabilityList = []

        for probability in probabilityList:
            cumulativeProbability += probability
            cumulativeProbabilityList.append(cumulativeProbability)

        return cumulativeProbabilityList


def main():
    """
    Creates items, then runs the simulation with the specified items and
    subsequently plots.
    """
    iterations = 10000
    runs = 50

    item1 = Item(1/3, isWanted=False)
    item2 = Item(1/3, isWanted=True)
    item3 = Item(1/3, isWanted=True)
    itemsList = [item1, item2, item3]

    instance = Instance(itemsList)
    instance.plotSimulationProbabilities(runs, iterations)


if __name__ == "__main__":
    main()