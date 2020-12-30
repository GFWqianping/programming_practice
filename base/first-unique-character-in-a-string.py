"""
https://leetcode-cn.com/problems/first-unique-character-in-a-string/
387. 字符串中的第一个唯一字符
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
"""


def solution(s) -> int:
    word_map = {}
    for i, word in enumerate(s):
        if word_map.get(word):
            word_map[word][0] += 1
        else:
            word_map[word] = [1, i]
    for v, index in word_map.values():
        if v == 1:
            return index
    return -1


if __name__ == '__main__':
    while True:
        string1 = input()
        print(solution(string1))
