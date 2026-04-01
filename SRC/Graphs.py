import matplotlib.pyplot
import numpy

class graphs:
    def __init__(self,stats,stats_catagories):
        self.stats = stats
        self.stats_catagories = stats_catagories
    
    def piegraph(self,inputStats,InputCats):
        costs = np.array(Costslists)
        matplotlib.pyplot.pie(costs , labels = mylabels)
        matplotlib.pyplot.show()
