import java.util.HashMap;
import java.util.Map;

/**
 * This question can be solved by brute force or in linear time if author is a little clever.
 * The method visits every element in the list once. Once at the element check if we've previously seen
 * the number needed to complete the sum. If yes, we're done and if no then add to a list of previously seen and
 * continue.
 */
public class TwoSum_1 {
    public static int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> lookup = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (lookup.containsKey(target - nums[i])) {
                return new int[]{i, lookup.get(target - nums[i])};
            }
            lookup.put(nums[i], i);
        }
        return null;
    }
}
