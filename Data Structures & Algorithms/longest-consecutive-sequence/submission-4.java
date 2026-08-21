class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums.length < 1) return 0;
        if(nums.length == 1) return 1;
        Arrays.sort(nums);
        int longest_sequence = 1;
        int temp = 1;
        for(int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i-1] + 1) {
                temp++;
            }
            else if (nums[i] == nums[i-1]) {
                continue;
            }
            else {
                temp = 1;
            }
            longest_sequence = Math.max(temp, longest_sequence);
        }
        return longest_sequence;
    }
}
