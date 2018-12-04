import java.util.HashMap;
import java.util.Map;

/**
 * The main trick for this question is recognizing that the list of integers doesn't need to be in any
 * particular order for randomness and that deletion can be accomplished by moving the element to be
 * deleted to the back of the list and decrement the 'effective' size of the list.
 */
class InsertDeleteGetRandom_380 {

    int[] nums;
    int size;
    Map<Integer, Integer> lookup;

    /** Initialize your data structure here. */
    public InsertDeleteGetRandom_380() {
        nums = new int[1000000];
        size = 0;
        lookup = new HashMap<>();
    }

    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    public boolean insert(int val) {
        if (lookup.containsKey(val)) return false;

        nums[size] = val;
        lookup.put(val, size);
        size++;

        return true;
    }

    /** Removes a value from the set. Returns true if the set contained the specified element. */
    public boolean remove(int val) {
        if (!lookup.containsKey(val)) return false;

        int index = lookup.get(val);
        lookup.remove(val);
        size--;

        nums[index] = nums[size];
        nums[size] = 0;
        lookup.replace(nums[index], index);

        return true;
    }

    /** Get a random element from the set. */
    public int getRandom() {
        int index = (int) Math.floor(Math.random() * size);
        return nums[index];
    }
}

/**
 * Your InsertDeleteGetRandom_380 object will be instantiated and called as such:
 * InsertDeleteGetRandom_380 obj = new InsertDeleteGetRandom_380();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
