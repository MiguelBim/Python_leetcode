
#NUMBER PALINDROME
class Solution(object):

    def isPalindrome(self, num):

        str_num = str(num)
        original_index = 0
        flag = None

        for index in reversed(range(len(str_num))):
            if str_num[original_index] == '-':
                return False
            elif str_num[original_index] == str_num[index]:
                original_index += 1
                flag = True
            else:
                return False

        return flag


def main():
    solution = Solution()
    flag = solution.isPalindrome(-123)
    print(flag)

if __name__ == '__main__':
    main()
