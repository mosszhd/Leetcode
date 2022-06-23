class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        words = ""
        for i in strs:
            words = words + str(len(i)) + "#" + i
        return words
    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        words = []
        # write your code here
        i = 0
        while(i < len(str)):
            j = i
            while(str[j] != '#'):
                j += 1
            length = int(str[i:j])
            words.append(str[j+1 : length+j+1])
            i = length + j + 1
        return words


sol = Solution()
print(sol.decode(sol.encode(["lint","code","love","you"])))
