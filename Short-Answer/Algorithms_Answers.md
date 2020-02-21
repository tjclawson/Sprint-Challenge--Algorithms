#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The complexity is O(n) even though n^3 is the range for the while loop because n^2 is added to a each loop, meaning
that the range is really n^3 - n^2, or n^1, which is n.


b) The complexity is O(n^2) because there are nested loops with n as the range, so for each n, it has to iterate 
approximately n times.


c) The complexity is O(n) because the function decrements and calls itself one time, meaning it goes through all
the data only once.

## Exercise II
1) Set max and min floors to highest and lowest floors, respectively
2) Find middle floor as max - min / 2 and round down
3) Go to middle floor and drop egg, if it breaks, set the new max floor to my current middle floor - 1, if 
    doesn't break, set my new min floor to my current floor + 1. Set the new middle floor as 
    current middle floor +/- ((max - min) / 2), adding if the egg doesn't break, subtracting if it does
4) Repeat steps 3 til the max floor is min + 1, and then we will know that f = max floor

The time complexity will be O(log n) because it is essentially a binary search.


