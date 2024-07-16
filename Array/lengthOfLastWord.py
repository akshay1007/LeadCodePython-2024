class Solution:
    def find_length(self,s):
        words = s.strip().split(' ')
        last_word = words[len(words)-1]
        print(len(last_word))


if __name__ == "__main__":
    obj = Solution()
    s = "   fly me   to   the moon  "
    obj.find_length(s)