import unittest

def euclidean_distance(p, q):

    #make sure both array are in the same dimension
    assert len(p) == len(q)  

    return max([abs(x-y) for x,y in zip(p,q)])


def euclidean_distance_procedural(p, q):

    #make sure both array are in the same dimension
    assert len(p) == len(q)  
   
    d = 0  

    for x,y in zip(p,q):

        d = max(d, abs(x-y))  

    return d

class BinarySearchTest(unittest.TestCase):

      def test_basic(self):
          self.assertEquals(euclidean_distance([1,2,3],[4,5,7]), 4) 
          self.assertEquals(euclidean_distance([1,2,3],[9,10,17]), 14) 
          self.assertEquals(euclidean_distance_procedural([1,2,3],[4,5,7]), 4) 
          self.assertEquals(euclidean_distance_procedural([1,2,3],[9,10,17]), 14) 


if __name__ == '__main__':

      unittest.main()  
