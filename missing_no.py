def missing_no(nums):
    return -1 * (sum(nums) - sum(range(0, 101)))
#     for i, element in enumerate(nums):
#         if i == element:
#             nums[i] = None
#     return nums
