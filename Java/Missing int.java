import java.util.Arrays;
class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int running = 0;
        for (int i : nums){
            running += i;
        }
        return (n*(n+1))/2 - running;
    }
}