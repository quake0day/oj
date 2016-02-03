"""
Definition of ArrayReader:
class ArrayReader:
    def get(self, index):
        # this would return the number on the given index
        # if there is no number on that index, return -1
"""
class Solution:
    # @param {ArrayReader} reader: An instance of ArrayReader 
    # @param {int} target an integer
    # @return {int} an integer
    def searchBigSortedArray(self, reader, target):
        # write your code here
        if reader == None:
            return -1
        end = 0
        while reader.get(end) < target and end < len(
        start = 0
        