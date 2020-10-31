---
title: "Segment_trees"
date: 2020-10-31T17:04:43+11:00
draft: false
---

# Segment Trees #

## Definition ##

    Segment tree is used for querying a property over a range of intervals. They are most efficient when you want to want to do repeated range queries. Let make the concept a bit concrete.

    Let's consider an array with 10 numbers in it. Our task is to find a minimum in an interval, such as get the index of minimum element in range (2,10).

    ```
    List of numbers: [1,19,3,5,6,3,2,44,22]
    Task: find minumum number between index 3-9 i.e find minumum in [3,5,6,3,2,44,22,3]
    Answer: 2
    ```
    A naive approach is to just iterate the array from index 3 to 9 and pick the minimum. Which works fine when the size of the array is small or we only need to do a single query. If we have an array of size 10,000 and we want to do 50 such queries: Then you might feel this method is very slow as each query is taking O(n) time.

    We can decrease the time to query from O(n) to O(log(n)) by using segment trees.

    It essentially pre-computes the result from some intervals while building the tree i.e in the stage when we are inserting the items in Segment tree. Which leads to saving some space and compute while during the time of querying.

    They are very similar to dyadic intervals. Is it the same thing??

## Ways to implement Segment tree ##

    There is primarily two way to implement a segment tree.

    1. Using an Array. Generally, segment trees take maximum space of
       4n

    2. We can also implement segment trees using Node and tree structure.

   Segment trees are easier to create maintain and update using a recursive algorithm, mainly because it's a tree.

We are basically precomputing the result while the creation of the tree since we know which query or property we are interested in.

