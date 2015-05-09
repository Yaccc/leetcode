__author__ = 'xiezhaodong'
'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 02 = 1
'''

class Solution:
    # @param {integer} n
    # @return {boolean}
    hashmap={}
    i=0
    def isHappy(self, n):
        self.i+=1
        print "-------------------------------------"
        print "enter func ",self.i,"value is -->",n
        array=[]
        string_char=str(n)
        #print string_char, type(string_char)
        str_len=len(string_char)
        for key in range(str_len):
            value_int=int(string_char[key])
            array.append(value_int)
            #get char each key
            #self.hashmap[key]=True
        if self.getMapValue(n) is True :
                return False
        new_sum=self.isIterOK(array)#get sum
        if new_sum==1:
            return True
        else:
            return self.isHappy(new_sum)

    def getMapValue(self,key):
        value=False
        try:
            value=self.hashmap[key]#is exist
        except:
            self.hashmap[key]=True
            #value=False
        return value

    def isIterOK(self,array):
        sum=0
        for key in array:
            #self.hashmap[key]=True
            print "now print key is:-->",key
            sum+=key*key
        print "the sum now is-->",sum
        return sum


so=Solution()
print so.isHappy(13)