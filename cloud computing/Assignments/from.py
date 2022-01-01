from typing import Callable, List 
import math

class DistanceFuncs:
    def calc_distance(self, point_a : List[float], point_b: List[float], dist_func: Callable,/)->float:
        """ Calculates distance between two points using the passed dist_func """
        return dist_func(point_a, point_b)

@staticmethod
def euclidean(point_a: List[float], point_b: List[float],/)->float:
    """
Calculates Euclidean Distance between two points Example:
>>> DistanceFuncs.euclidean([1,1],[1,1]) 
0.0
"""
    return math.dist(point_a, point_b) 

@staticmethod
def manhattan_distance(point_a: List[float], point_b: List[float],/):
    """Compute the manhattan_distance between two points"""
    raise NotImplementedError()

@staticmethod
def jaccard_distance(point_a: List[float], point_b: List[float],/):
    """Compute the jaccard_distance between two points"""
    raise NotImplementedError()

def main():
    """Demonstrate the usage of DistanceFuncs """
    pass

if __name__ =="__main__":
    main()
    
