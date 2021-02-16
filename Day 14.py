class Difference:
    def __init__(self, a):
        self.__elements = a
    # Add your code here
    def computeDifference(self):
        # instance variable
        self.maximumDifference = 0
        size = len(self.__elements)
        for i in range(size):
            for j in range(i+1, size):
                difference = abs(self.__elements[i] - self.__elements[j])
                if difference > self.maximumDifference:
                    self.maximumDifference = difference
            
        

# End of Difference class