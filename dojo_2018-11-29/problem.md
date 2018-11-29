# The Time in Words

https://www.hackerrank.com/challenges/the-time-in-words/problem

Given the time in numerals we may convert it into words,
as shown below:

5:00 -> five o' clock
5:01 -> one minute past five
5:10 -> ten minutes past five
5:15 -> quarter past five
5:30 -> half past five
5:40 -> twenty minutes to six
5:45 -> quarter to six
5:47 -> thirteen minutes to six
5:28 -> twenty eight minutes past five

At minutes = 0, use o'clock. For 1 <= minutes <= 30, use past,
and for 30 < minutes use to.
Note the space between the apostrophe and clock in o' clock.
Write a program which prints the time in words
for the input given in the format described.


## Function Description

Complete the timeInWords function in the editor below.
It should return a time string as described.

timeInWords has the following parameter(s):

* h: an integer representing hour of the day
* m: an integer representing minutes after the hour


## Input Format

The first line contains h, the hours portion
The second line contains m, the minutes portion


## Constraints

* 1 <= h <= 12
* 0 <= m < 60


## Output Format

Print the time in words as described.


## Sample Input 0

5
47


## Sample Output 0

thirteen minutes to six


## Sample Input 1

3
00


## Sample Output 1

three o' clock


## Sample Input 2

7
15


## Sample Output 2

quarter past seven
