# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

class Solution(object):
    def romanToInt(self, roman_num):

        int_num = 0
        nums_dict = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100,  'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
        length = len(roman_num)
        flag = None

        for index in range(length):

            if flag:
                flag = False
                continue

            advance_index = index + 1
            actual_num = roman_num[index]
            if advance_index < length:
                if nums_dict[actual_num] >= nums_dict[roman_num[advance_index]]:
                    int_num += nums_dict[actual_num]
                else:
                    combined_num = roman_num[index:advance_index + 1]
                    int_num += nums_dict[combined_num]
                    flag = True
            else:
                int_num += nums_dict[actual_num]

        print(int_num)


def main():
    solution = Solution()
    solution.romanToInt('XXXIV')


if __name__ == '__main__':
    main()