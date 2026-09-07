from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #given: an array of strings strs
        #return: a list of lists where all anagrams are grouped together into sublists 
        #solution: create a dictionary of frequency of each character, if the current word dictionary isn't in 
        #the list of lists, create a new sublist of it, otherwise add to a list with the one with the same one 

        curr_frequency = {}
        frequencies = {}
    
        for i in strs: 
            curr = "".join(sorted(i))
            if curr in frequencies: 
                frequencies[curr].append(i)
            else: 
                frequencies[curr] = [i]

        return list(frequencies.values())