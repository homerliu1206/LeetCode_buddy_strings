class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        list_s = list(s)
        list_g = list(goal)

        if len(list_s) == 1: # cannot switch >> must be false
            print(False)
            # return False

        elif len(list_s) == 2:
                if list_s == list_g[::-1]:
                    print(True)
                    # return True
                else:
                    print(False)
                    # return False

        elif len(list_s) >= 3:
            index_dif = []
            i = 0
            while i < len(list_s):
                if list_s[i] != list_g[i]:
                    index_dif.append(i)
                i += 1
            # print(index_dif)

            if len(index_dif) > 2:
                print(False)
                # return False

            elif len(index_dif) == 2:
                if list_s[index_dif[0]] == list_g[index_dif[1]] and list_s[index_dif[1]] == list_g[index_dif[0]]:
                    print(True)
                    # return True
                else:
                    print(False)
                    # return False

            elif len(index_dif) == 0: # all elements are the same
                list_count = []
                for i in set(list_s):
                    if list_s.count(i) >= 2:
                        list_count.append(i)
                if bool(list_count) == True:
                    print(True)
                    # return True
                else:
                    print(False)
                    # return False

solution = Solution()
solution.buddyStrings(s = "ab", goal = "ab")

# Input: s = "ab", goal = "ba"
# Output: true

# Input: s = "abcd", goal = "cbad"
# Output: true

# Input: s = "ab", goal = "ab"
# Output: false

# Input: s = "aa", goal = "aa"
# Output: true

# Input: s = "aa", goal = "aa"
# Output: true

# Input: s = "abab", goal = "abab"
# Output: true

# Input: s = "aaab", goal = "aaab"
# Output: true

# Input: s = "a", goal = "a"
# Output: false

