https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/holiday-season-ab957deb/

It's a holiday season for all school students around the world! Unfortunately, Mahamba is busy preparing for International Olympiad in Informatics, which will be held in Tehran, Iran. He is now facing a new challenge from his teacher Aceka, and it goes something like this:

You have a string 
x
x of length 
N
N, which consists of small English letters. You have to find the number of indexes 
a
a, 
b
b, 
c
c and 
d
d, such that 
1
<=
a
<
b
<
c
<
d
<=
N
1<=a<b<c<d<=N and 
x
a
==
x
c
xa==xc, as well as 
x
b
==
x
d
xb==xd.

He is baffled and definitely needs some help. So, you, the best programmer in Lalalandia, decided to give him a hand!

Input format

The first line contains the number 
N
N - the length of a string 
x
x. The second line contains the string 
x
x itself.

Output format

The first and only line should contain the answer to the problem.

Constraints

1
<=
N
<=
2000
1<=N<=2000
The string 
x
x only contains small English letters.

SAMPLE INPUT 
5
ababa
SAMPLE OUTPUT 
2
Explanation
There are only 2 variants: (a=1,b=2,c=3,d=4) and (a=2,b=3,c=4,d=5)