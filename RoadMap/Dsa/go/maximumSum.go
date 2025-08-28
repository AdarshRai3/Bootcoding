package main

func maximumSum(nums []int) int{
	maxSum, currSum := nums[0], nums[0]
	for i:=1 ;i<len(nums);i++{
		currSum = max(currSum, currSum+nums[i])
		maxSum = max(maxSum, currSum)
	}
	return maxSum
}

func max(a,b int) int{
	if a>b{
		return a
	}
	return b
}