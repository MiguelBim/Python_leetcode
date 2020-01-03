# https://leetcode.com/problems/reverse-integer/

#REVERSE INTEGER
class Solution(object):

    def reverse(self, integer):

        if -2**31 < integer < (2**31)-1:

            str_val = str(integer)
            str_val = str_val[::-1]
            if str_val[-1] == '-':
                str_val = '-' + str_val[0:-1]
                result = int(str_val)
            else:
                result = int(str_val)
            print(result)
            if -2**31 < result < (2**31)-1:
                return result
            else:
                return 0

        else:
            return 0


def main():

    solution = Solution()
    solution.reverse(-123)


if __name__ == '__main__':
    main()
