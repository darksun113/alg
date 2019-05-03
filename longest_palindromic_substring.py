class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        max = 0
        result = ""
        for i in range(0,l):
            for size in range(0,l-i+1):
                right = i + size
                if(right>=l):
                    break
                isPalindrome = False
                #print(s[i:right+1])
                if(size == 0):
                    isPalindrome = True
                elif(size == 1):
                    isPalindrome = (s[i]==s[right])
                else:
                    mid = i + size/2
                    j = i
                    k = right
                    while(j<=mid):
                        ####
                        #print(s[j],s[k])
                        if(s[j]!=s[k]):
                            break
                        j+=1
                        k-=1
                    if(j>mid):
                        isPalindrome = True
                if(isPalindrome==True):
                    if(size+1>=max):
                        max = size+1
                        if(size == 0):
                            result = "".join(s[i])
                        elif(size == 1):
                            result = "".join(s[i:i+2])
                        else:
                            result = "".join(s[i:right+1])
        return result

s = Solution()
print(s.longestPalindrome("adam"))
print(s.longestPalindrome("babad"))
print(s.longestPalindrome("a"))
print(s.longestPalindrome("cbbd"))
print(s.longestPalindrome("ccc"))