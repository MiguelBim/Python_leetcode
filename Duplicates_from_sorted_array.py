
#DUPLICATES IN SORTED ARRAY
class Solution(object):

    def removeDuplicates(self, nums_list):

        for index in range(len(nums_list) - 1):
            print(index)
            if nums_list[index] == nums_list[index + 1]:
                continue
            else:
                nums_list.pop(index)
                index -= 1
            print(nums_list)


def main():

    solution = Solution()
    solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])


if __name__ == '__main__':

    main()
