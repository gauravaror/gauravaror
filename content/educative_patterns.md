---
title: "Educative patterns"
date: 2020-01-17T20:18:52+11:00
draft: false
---

Maintaining list Inspired from list maintained by [sadihassan](https://sadihassan.github.io/leetlist/educative_pattern.html)

## Pattern : Sliding Window (07)

| Title | Link| Code | Notes |
| ------ | ---- |------ | -----------|
| Fruits into baskets (medium) |[Leet](https://leetcode.com/problems/fruit-into-baskets/) | [github](https://github.com/gauravaror/programming/blob/master/fruit_in_basket.py) | Sliding window, check at end of if condition |


## Pattern : Two pointers

| Title | Link | Code  | Notes |
| ----- | ---- | ---- |  ----- |
| Pair with Target Sum (easy) | [Leet](https://leetcode.com/problems/two-sum/) | [github](https://github.com/gauravaror/programming/blob/master/two_sums.py) |hashing solution and two pointers |


## Pattern : Fast and Slow pointers:

| Title | Link | Code  | Notes |
| ----- | ---- | ---- |  ----- |
| Linked list Cycle | [Leet](https://leetcode.com/problems/linked-list-cycle/) | [github](https://github.com/gauravaror/programming/blob/master/linked_list_cycle.py) | Fast and slow pointer and hash tables |
| Start of Linked list Cycle | [Leet](https://leetcode.com/problems/linked-list-cycle-ii/) | [github](https://github.com/gauravaror/programming/blob/master/linked_list_cycle_entry_point.py) | Fast and slow point approach and also hash based works works. Pointer approach also does entry to meeting point traversal after meeting point |
| Happy Number | [Leet](https://leetcode.com/problems/happy-number/) | [github](https://github.com/gauravaror/programming/blob/master/happy_number.py) | Fast and slow point approach and also hash based works works.|
| Middle of the Linked List | [Leet](https://leetcode.com/problems/middle-of-the-linked-list/) | [github](https://github.com/gauravaror/programming/blob/master/middle_of_linked_list.py) | Fast and slow point approach.|

## Pattern: Merge Intervals

| Title | Link | Code  | Notes |
| ----- | ---- | ---- |  ----- |
| Merge Intervals | [Leet](https://leetcode.com/problems/merge-intervals/) | [github](https://github.com/gauravaror/programming/blob/master/merge_intervals.py) | Sort the intervals and linear |


## Pattern: In-Place reversal of Linked List
| Title | Link | Code  | Notes |
| ----- | ---- | ---- |  ----- |
| Reverse a Linked List (in-place) | [Leet](https://leetcode.com/problems/reverse-linked-list/) | [github](https://github.com/gauravaror/programming/blob/master/reverse_linked_list.py) | Save the current element before moving on to the next element |
| Reverse a sublist in Linked List | [Leet](https://leetcode.com/problems/reverse-linked-list-ii/) | [github](https://github.com/gauravaror/programming/blob/master/linked_list_reverse_2.py) | Store the first and then adjust the list |

## Pattern: Tree Breadth First Search
| Title | Link | Code  | Notes |
| ----- | ---- | ---- |  ----- |
| Level Order traversal of Binary Tree | [Leet](https://leetcode.com/problems/binary-tree-level-order-traversal/) | [github](https://github.com/gauravaror/programming/blob/master/binary-tree-level-order-traversal.py) | Binary Tree Level order Traversal use the BFS and maintain level |
| Level Order traversal of Binary Tree  reverse | [Leet](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/) | [github](https://github.com/gauravaror/programming/blob/master/binary-tree-level-order-traversal_2.py) | Binary Tree Level order Traversal use the BFS and maintain level Just reverse the list from last question |


## Pattern: Tree Depth First Search
| Title | Link | Code  | Notes |
| ----- | ---- | ---- |  ----- |
| Path Sum | [Leet](https://leetcode.com/problems/path-sum/) | [github](https://github.com/gauravaror/programming/blob/master/path-sum.py) | Path Sum using dfs and if leaf matches the sum exit else continue |
| Path Sum return all path | [Leet](https://leetcode.com/problems/path-sum-ii/) | [github](https://github.com/gauravaror/programming/blob/master/path-sum-ii.py) | Path Sum using dfs and if leaf matches the sum exit else continue Same as above just pass lis of all nodes val till root and append in answer|



## Pattern: Two Heaps
| Title | Link | Code  | Notes |
| ----- | ---- | ---- |  ----- |
| Find the Median of a Number Stream (hard)| [Leet](https://leetcode.com/problems/find-median-from-data-stream/) | [github](https://github.com/gauravaror/programming/blob/master/find_median_sort_two_heap.cpp) | Maintain a min and max heap and take top elements based on sizes of heap and keep them balanced. |
| Sliding Window Median (hard) [Not Finished]| [Leet](https://leetcode.com/problems/sliding-window-median/) | [github](https://github.com/gauravaror/programming/blob/master/sliding-window-median-failed.cpp) | Maintain a min and max heap and take top elements based on sizes of heap and keep them balanced. |
| Mazimize Capital (hard)| [Leet](https://leetcode.com/problems/ipo/) | [github](https://github.com/gauravaror/programming/blob/master/ipo.cpp) | Maintain max heap for profit and min heap for capital not matching and add all capital. |


# Non-Educative pattern Questions

## Patter: Dynamic Programming
Dynamic programming is all about saving the computation by saving the old computation. This is enabled by maintaining a table to save the previous computation and generally results in a faster algoritm.

| Title | Link | Code  | Notes |
| ----- | ---- | ---- |  ----- |
| | Minumum Path Sum [Leet](https://leetcode.com/problems/minimum-path-sum/) | [github](https://github.com/gauravaror/programming/blob/master/minimum-path-sum-dp.cpp) | Sum first row and column incrementally and then take minimum from left and right path incrementally. Maintain in same table. It is also possible to do this problem using DFS and shortest path algorithm |


