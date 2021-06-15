def smallest_subarray_with_given_sum(S, nums):

  window = 0
  start = 0
  min_ = math.inf

  for end in range(len(nums)):
      window += nums[i]
      while window >= S:
          min_ = min(min_, end - start + 1)
          window -= nums[start]
          start += 1
  if min_ == math.inf:
    return 0
   
   return min_
        
