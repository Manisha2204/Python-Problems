# 🐍 Python Problem Solving — Day 1

## 1. Count Even Numbers

**Approach:**
Loop through each number and check whether it is divisible by `2`. If yes, increase the counter.

**Example:**

```text
Input: 1 2 3 4 6
Output: 3
```

**Explanation:**
The even numbers are `2, 4, 6`, so the count is `3`.

---

## 2. Sum Positive Numbers

**Approach:**
Start with `total = 0`. Loop through the numbers and add a number to `total` only when it is positive.

**Example:**

```text
Input: -2 5 10 -3 4
Output: 19
```

**Explanation:**
Positive numbers are `5, 10, 4`. Their sum is `19`.

---

## 3. Find Largest Number

**Approach:**
Take the first number as the initial largest value. Compare every other number with it and update the largest value whenever a bigger number is found.

**Example:**

```text
Input: 4 8 2 15 6
Output: 15
```

**Explanation:**
`15` is the largest number in the list.

---

## 4. Count Occurrences

**Approach:**
Loop through the list and compare every number with the target. Increase the counter whenever they are equal.

**Example:**

```text
Input: 2 5 2 7 2 8
Target: 2
Output: 3
```

**Explanation:**
The number `2` appears `3` times.

---

## 5. Find Smallest Number

**Approach:**
Take the first number as the initial smallest value. Compare every other number and update the smallest value whenever a smaller number is found.

**Example:**

```text
Input: 8 3 10 1 6
Output: 1
```

**Explanation:**
`1` is the smallest number in the list.

---

## 6. Reverse a List

**Approach:**
Use indexes to access the list from the last position to the first and add each element to a new list.

**Example:**

```text
Input: 1 2 3 4 5
Output: 5 4 3 2 1
```

**Explanation:**
The elements are accessed in reverse index order.

---

## 7. Count Positive, Negative and Zero

**Approach:**
Use three separate counters. For every number, check whether it is positive, negative, or zero and increase the corresponding counter.

**Example:**

```text
Input: -2 5 0 -7 3 0
Output: (2, 2, 2)
```

**Explanation:**
There are `2` positive numbers, `2` negative numbers, and `2` zeros.

---

## 8. Find Second Largest Distinct Number

**Approach:**
Maintain two values: `largest` and `second`. When a new largest number is found, move the old largest into `second`. Ignore duplicate values.

**Example:**

```text
Input: 10 5 8 10 3
Output: 8
```

**Explanation:**
The largest distinct number is `10`, so the second largest distinct number is `8`.

---

## 9. Remove Duplicates Without `set()`

**Approach:**
Create a new list. For every number, check whether it is already present in the new list. Add it only if it is not present.

**Example:**

```text
Input: 1 2 2 3 1 4
Output: 1 2 3 4
```

**Explanation:**
Repeated values are skipped, while the first occurrence is kept.

---

## 10. Find Index of a Target

**Approach:**
Loop through the indexes of the list. If the value at an index matches the target, return that index. If it is never found, return `-1`.

**Example:**

```text
Input: 10 20 30 40
Target: 30
Output: 2
```

**Explanation:**
`30` is located at index `2`.

---

## 11. Sum Values at Even Indexes

**Approach:**
Loop through the indexes and check whether the index is even using `% 2`. If it is even, add the corresponding value.

**Example:**

```text
Input: 10 20 30 40 50
Output: 90
```

**Explanation:**
Even indexes are `0, 2, 4`.

```text
Index:  0   1   2   3   4
Value: 10  20  30  40  50
```

So:

`10 + 30 + 50 = 90`

---

## 12. Find Largest Even Number

**Approach:**
Use `None` initially to represent that no even number has been found. For every even number, update the maximum if it is the first even number or is larger than the current maximum.

**Example:**

```text
Input: -8 -4 -12
Output: -4
```

**Explanation:**
`-4` is the largest even number. Using `None` instead of `-1` also allows negative even numbers to work correctly.

---

## 13. Count Numbers Greater Than Average

**Approach:**
First calculate the total of all numbers and divide it by the number of elements to get the average. Then loop again and count numbers greater than the average.

**Example:**

```text
Input: 10 20 30 40 50
Average: 30
Output: 2
```

**Explanation:**
Only `40` and `50` are greater than the average.

---

## 14. Count Duplicate Numbers

**Approach:**
Use one set called `seen` to remember numbers already encountered. If a number is already in `seen`, add it to a `duplicates` set. Since a set stores each value only once, repeated occurrences are counted as one duplicate number.

**Example:**

```text
Input: 1 2 2 3 3 3 4
Output: 2
```

**Explanation:**
`2` and `3` appear more than once, so there are `2` duplicate numbers.

---

## 15. Find Most Frequent Number

**Approach:**
First create a dictionary to store the frequency of every number. Then loop through the dictionary and keep track of the number with the highest count.

**Example:**

```text
Input: 1 2 2 3 3 3 4
Output: 3
```

**Explanation:**

The frequency dictionary becomes:

```text
1 → 1
2 → 2
3 → 3
4 → 1
```

Since `3` has the highest frequency, the answer is `3`.
