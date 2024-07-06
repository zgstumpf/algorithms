There are many games that involves merging numbers into bigger ones. For example, in the game 2048, players can merge a 2 block with a 2 block to get a 4 block or a 16 block with a 16 block to get a 32 block. In this case, merging results in 2x the value. In other games, merging results in the value + 1. For example, a 3 and 3 merge into a 4. 

In the value + 1 scenarioe, the numbers are not fully merged until no more merges can be performed. For example, a 2, 2, and 3 can merge once into 3 and 3 and again into 4.

When I was an experienced programmer, I tried to code an algorithm in C# to fully merge a list of numbers. The code is in merge-v1.cs. (The commit date is not accurate to when it was coded since the file was added to this repository at a later date.) The code is absolutely terrible since at this point I had no education in algorithms. A few days later, I wrote better looking C# code in merge-v2.cs, but I used functions I didn't even fully understand at the time, and the time/space complexity is not optimized since at this time I had no education in optimizing time/space. 

A few years later when I studied data structures & algorithms as a personal project, I attempted this task again, but this time I used Python. The code is found in merge.py, and it is significantly more optimized and readable than my previous attempts. It is O(n) time and O(n) space since it uses a set to allow constant-time access when searching for a number to merge. 

I included this code and story to show the evolution of my programming over just a couple years. 
