'''
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".
'''
class Solution(object):
    def defangIPaddr(self, address):
        return address.replace(".", "[.]")





'''
You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.
'''
class Solution(object):
    def interpret(self, command):
        return command.replace("()", "o").replace("(al)", "al")





'''
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.
'''
class Solution(object):
    def numIdenticalPairs(self, nums):
        number = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] == nums[j] and j > i:
                    number += 1
        return number





'''
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
'''
class Solution(object):
    def largestAltitude(self, gain):
        alts = [0]
        for i in range(len(gain)):
            alts.append(alts[i] + gain[i])
        return max(alts)





'''
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
'''
class Solution(object):
    def subtractProductAndSum(self, n):
        summ = 0
        product = 1
        while n > 0:
            summ += n % 10
            product *= n % 10
            n //= 10
        return product - summ