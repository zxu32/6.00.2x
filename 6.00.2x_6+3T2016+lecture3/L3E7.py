from lecture3segment3.lecture3_segment3 import *


class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        Edge.__init__(self, src, dest)
        self.weight = weight

    def getWeight(self):
        return self.weight

    def __str__(self):
        return Edge.__str__(self) + '(' + str(self.getWeight()) + ')'
