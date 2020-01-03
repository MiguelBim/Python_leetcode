# https://leetcode.com/problems/two-sum/


#SUMA DE DOS NUMEROS CON UN TARGET
class Solution(object):

    def twoSum(self, nums, target):

        solution = []

        for index in range(len(nums)):
            val_needed = target - nums[index]
            values = nums[:]
            values.pop(index)
            options = values
            if val_needed in options:
                for index_2 in range(len(nums)):
                    if nums[index_2] == val_needed and nums[index] != nums[index_2]:
                        solution.extend([nums[index], nums[index_2]])


        print (solution)


def main():

    solution = Solution()
    solution.twoSum([2,7,1,15], 9)

if __name__ == '__main__':
    main()


