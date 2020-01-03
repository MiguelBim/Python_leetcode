
#VALID PARENTESIS
class Solution(object):

    def isValid(self, str):
        open = ['(', '{', '[']
        close = [')', '}', ']']
        stack = []

        for character in str:
            if character in open:
                stack.append(character)
            elif character in close:
                if len(stack) <= 0:
                    return False
                if open.index(stack.pop()) != close.index(character):
                    return False

        return len(stack) == 0


class main():

    solution = Solution()
    solution.isValid('([])')


if __name__ == '__main__':
    main()
