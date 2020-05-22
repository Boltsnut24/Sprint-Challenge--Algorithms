#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)


b) O (n log(n))


c) O(n)

## Exercise II

1. Drop an egg from the middle floor
2. If the egg breaks, go down half the number of floors you are from the ground and drop another. If this egg breaks repeat this step until it does not.
3. If an egg does not break, go up in floors until you are mid way between the floor you dropped this egg from and the lowest floor an egg has broken from.
4. repeat steps 1/2 as necessary until there are no floors left you haven't dropped an egg from that fit within that range. At this point, the highest floor you have dropped an egg from is floor f.

Runtime is O(log n)

