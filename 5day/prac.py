####################################
# 중복 문자가 없는 가장 긴 부분 문자열
# 앞자리부터 하나씩 검사해서 중복되지않는 값의 최대 길이를 찾아내는 문제 (연속으로 이어져야함)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: #ex)"a b c a b c b b"
        word = set() #set함수 사용
        l = 0 #길이의 위치를 찾기위한 index
        r = 0 # result
        for i in range(len(s)): #s에 들어간 string의 값의 길이만큼 for문 실행 ex)0~7번 8번
            while s[i] in word: # word내부의 해당 s[i]의 값이 존재하면 => 중복된값이 있을경우 while문 돌아감 ex)a 가 word에 있는가
                word.remove(s[l]) 
                l += 1 
            word.add(s[i]) #중복된 값이 없는것은 word에 넣어줌 ex) [ ,  ,  , b b]
            r = max(r, i - l + 1) #ex) 7 - 5 + 1 = 3
        return r

import sys
input = sys.stdin.readline()
n, m = map(int, input.split())
data = {}

for _ in range(n):
    site, pw = input.split()
    data[site] = pw

for _ in range(m):
    input_site = input
    print(data[input_site])