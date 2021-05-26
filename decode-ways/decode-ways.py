class Solution(object):
    
    def numDecodings(self, s) -> int:
        """
        :type s: str
        :rtype: int
        """
        previous_number_of_ways=0
        number_of_ways=int(s>'')
        previous_digit=''
    
        for digit in s:
            copy_previous=previous_number_of_ways
            previous_number_of_ways=number_of_ways

        #check if the current digit is greater than zero
        #If it is, then (digit>'0') becomes true, and we multiply that by the total number of ways so far
        #...Think permutations
            number_of_ways=(digit>'0')*number_of_ways
        
        #At the same time, we check if the current digit and the next digit, are less than 27..
        #If they are, then its another permutation possibility
        #Again, we are checking the truth, and multiplying it by the number of previously known was, not
        #the current number of ways
        #
        #We have the 9< check because if the digit we are on is a zero, then we won't count the 
        #next permutation
            number_of_ways+= (9<int(previous_digit+digit)<27)*copy_previous

        #Finally, remember that our last digit was the digit we are on now
            previous_digit=digit
        
        return number_of_ways