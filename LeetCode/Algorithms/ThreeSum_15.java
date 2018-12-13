import java.util.*;

/**
 * This question can be solved in quadratic time by using the reduction of 2 sum.
 * The method visits every element in the list once. Once at the element we calculate the 2 sum of the remaining
 * elements in the list.
 */
public class ThreeSum_15 {
    public static List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> solutions = new ArrayList<>();
        List<Integer> numbers = new ArrayList<>();
        for (int num : nums) {
            numbers.add(num);
        }
        Collections.sort(numbers);

        for (int i = 0; i < numbers.size(); i++) {
            if (i > 0 && numbers.get(i).equals(numbers.get(i - 1))) continue;
            List<List<Integer>> ans = twoSum(numbers, -numbers.get(i), i);
            for (List<Integer> a: ans) {

                List<Integer> solution = new ArrayList<>();

                solution.add(a.get(0));
                solution.add(a.get(1));
                solution.add(numbers.get(i));

                solutions.add(solution);
            }
        }
        return solutions;
    }

    private static List<List<Integer>> twoSum(List<Integer> nums, int target, int forbidIndex) {
        Map<Integer, Integer> lookup = new HashMap<>();
        Set<List<Integer>> solutions = new HashSet<>();
        for (int i = forbidIndex + 1; i < nums.size(); i++) {
            if (lookup.containsKey(target - nums.get(i))) {
                List<Integer> solution = new ArrayList<>();
                solution.add(nums.get(i));
                solution.add(nums.get(lookup.get(target - nums.get(i))));
                solutions.add(solution);
            }
            lookup.put(nums.get(i), i);
        }
        return new ArrayList(solutions);
    }
}
