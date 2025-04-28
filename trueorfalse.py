 #nums = list(map(int, input().split()))
#def has_duplicates(nums):
   # for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] == nums[j]:
#                 return True
#     return False

# print(has_duplicates(nums))

nums=list(map(int,input().split()))
def has_duplicates(nums):
    if (len(nums))!=(len(set(nums))):
        return True
    else:
        return False
print(has_duplicates(nums))
