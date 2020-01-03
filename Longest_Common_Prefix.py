class Solution(object):
    #LONGEST COMMON PREFIX
    def longestCommonPrefix(self, str_list):

        if len(str_list) != 0:

            shortest_word = str_list[0]
            str_list.sort(key=len)
            print(str_list)

            for word in str_list:
                word_len = len(word)
                if word_len < len(shortest_word):
                    shortest_word = word
                else:
                    continue


            print('The shortest word is: ' + shortest_word)

            prefix = ''

            for index in range(len(shortest_word)):
                # print(index)
                flag = False
                for word in str_list[1:]:
                    # print(word)
                    if shortest_word[index] == word[index]:
                        if index == 0:
                            print(word)
                            print(shortest_word[index])
                            print(word[index])
                        flag = True
                    else:
                        flag = False
                if flag:
                    prefix += shortest_word[index]

        else:
            prefix = ''

        print('The prefix is: ' + prefix)


def main():

    solution = Solution()
    solution.longestCommonPrefix(["abab","aba","abc"])

if __name__ == '__main__':
    main()
