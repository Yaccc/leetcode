/*
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
*/


public int[] twoSum(int[] numbers, int target) {
        int length=numbers.length;//长度
    	HashMap<Integer, Integer> nums=new HashMap<Integer, Integer>();

    	for(int i=0;i<length;i++){
    		Integer first=nums.get(target-numbers[i]);
    		if(first!=null){

    			return new int[]{first,i+1};
    		}
    		nums.put(numbers[i], i+1);
    		}

        return null;
}