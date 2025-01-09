public ArrayList<Integer> findTwoElement(int[] arr) {
    ArrayList<Integer> result = new ArrayList<>();
    int n = arr.length;

    // Step 1: Initialize XOR for both array elements and numbers from 1 to n
    int xor = 0;

    // XOR all elements in the array and numbers from 1 to n
    for (int i = 0; i < n; i++) {
        xor ^= arr[i];   // XOR array elements
        xor ^= (i + 1);  // XOR numbers from 1 to n
    }

    // Step 2: Find the rightmost set bit in xor
    int setBit = xor & -xor; // Rightmost set bit

    // Step 3: Divide numbers into two groups based on the set bit
    int x = 0, y = 0; // x and y will store the two elements (missing and duplicate)
    for (int i = 0; i < n; i++) {
        if ((arr[i] & setBit) != 0) {
            x ^= arr[i];
        } else {
            y ^= arr[i];
        }
        if (((i + 1) & setBit) != 0) {
            x ^= (i + 1);
        } else {
            y ^= (i + 1);
        }
    }

    // Step 4: Identify which is missing and which is duplicate
    int countX = 0;
    for (int value : arr) {
        if (value == x) {
            countX++;
        }
    }

    if (countX == 0) {
        result.add(y); // y is duplicate
        result.add(x); // x is missing
    } else {
        result.add(x); // x is duplicate
        result.add(y); // y is missing
    }

    return result;
}