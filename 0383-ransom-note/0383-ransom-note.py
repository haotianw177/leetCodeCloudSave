class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dictionary = {}

        for i in magazine:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1

        for i in ransomNote:
            if i in dictionary and dictionary[i] > 0:
                dictionary[i] -= 1
            else:
                return False
        return True

    
        