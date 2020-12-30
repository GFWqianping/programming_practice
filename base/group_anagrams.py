"""
https://leetcode-cn.com/problems/group-anagrams/
字母异位词分组
9660ms 5%
19.9MB 5%
"""


def word2count_dict(word):
    count_dict = {}
    for p in word:
        count_dict[p] = count_dict.get(p) + 1 if count_dict.get(p) else 1
    return count_dict


def count_equal(count1, count2):
    if len(count1) != len(count2):
        return False
    for k, v in count1.items():
        if count2.get(k) != v:
            return False
    return True


def groupAnagrams(strs):
    group_list = []
    count_list = []
    for word in strs:
        word_count = word2count_dict(word)
        added = False
        for ind, count in enumerate(count_list):
            if count_equal(count, word_count):
                if len(group_list) > ind:
                    group_list[ind] = group_list[ind] + [word] if group_list[ind] else [word]
                else:
                    group_list.append([word])
                added = True
                break
        if not added:
            count_list.append(word_count)
            group_list.append([word])
    return group_list


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(strs))
