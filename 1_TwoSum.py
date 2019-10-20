class Solution(object):
    """
    [2,7,11,15] and target = 9

    dict = {}
    - Initially our dictionary is empty
    - Traverse the entire list and check if target - nums[i] already in the
      dict or not
    - if yes, then it means that a pair with given sum exist else if entire array
    is traversed and still no pair is found, return [-1,-1]
    
    """
    def twoSum(self, nums, target):
        """
        :param nums: List[int]
        :param target: int
        :return: List[int]
        """
        mapper = {}
        for i in range(len(nums)):
            to_find = target - nums[i]
            if to_find in mapper:
                return [mapper[to_find], i]
            else:
                mapper[nums[i]] = i

        return [-1, -1]


if __name__ == "__main__":
    s = Solution()
    print("Output : {}".format(s.twoSum([2, 7, 11, 15], 9)))
