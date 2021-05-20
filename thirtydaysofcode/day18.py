# link to problem: https://www.hackerrank.com/challenges/30-queues-stacks/problem
# solution implemented as per source code
import sys
from collections import deque

class Solution:
    def __init__(self):
        self.stck = list()
        self.que = deque()

    def pushCharacter(self, ch):
        self.stck.append(ch)

    def enqueueCharacter(self, ch):
        self.que.append(ch)

    def popCharacter(self):
        return self.stck.pop()

    def dequeueCharacter(self):
        return self.que.popleft()


s = input()
obj = Solution()

l = len(s)
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break

if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")