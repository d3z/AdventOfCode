# AdventOfCode
My solutions for the adventofcode.com puzzles

## Day one

The first part of this problem can be solved using a simple reduce. You are, after all, trying to reduce the list of 
commands into a single value.

For the second part, I just kept a count of iterations in my reduce and set the basement value to the current count as 
soon as the floor hit -1.

## Day two
A couple of simple maths puzzles today. My solutions can very likely be cleaned up quite a bit.

## Day three
I don't mind telling you that the second bit of this puzzle had me scratching my head for a while. It turns out to be 
simple enough. I was definitely hampered a little by my solution to the first part which needed a bit of 
refactoring to work for the second one.

For the first part of the puzzle, we simply need to identify all the houses that are visited. I did this using 
(x,y) coordinates. This is an arbitrary decision. You could choose any other method. Then it's a matter of modifying
Santa's current position and keeping a count of all the visits to each coordinate.

The instructions for the second part were a little fuzzy, but it comes down to a bit of a refactor of the first part
to take turns over the same delivery map.

## Day four
Simple brute force check. There is, no doubt, a far more efficient way to calculate the hashes (in parallel for instance)
but, it works :)
