#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#need optimization
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        l = len(s)
        i = 0
        sublen = 0
        max_sub = 0
        chartable = [0]*256
        while(i<l):
            index = ord(s[i])
            if(chartable[index]==0):
                chartable[index]=1
                sublen+=1
                i += 1
            else:
                if(sublen>max_sub):
                    max_sub = sublen
                i = i - sublen + 1
                sublen = 0
                chartable = [0]*256
        return max(max_sub,sublen)


 

s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring("dvdf"))
with open("/Users/kelvin/Desktop/testinput.txt") as f:
    longstr = f.read()
    print(s.lengthOfLongestSubstring(longstr))
