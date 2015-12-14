# AdventOfCode
My solutions for the adventofcode.com puzzles.

I have, of course, been looking at other people's answers to the puzzles
after I complete them. Some of the solutions I've committed here are far from optimal solutions when compared to others.
I thought that I'd just keep my solutions though rather than 'fix' them based on what I read elsewhere.

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

## Day five
Pretty simple regexp puzzles. I'm no regexp master though so mine could probably be improved. Again, they worked :) The 
whole thing could very likely have been solved in a single regexp (one for each part of the puzzle at any rate) but I
think keeping them separate makes it a little more readable.

## Day six
I'm not overly happy with my solution here. I know there must be a way to do this without necessarily saving the
entire state, but I haven't had time today to work on it. I'll search for other solutions and copy ... ah, I mean, refactor.

## Day seven
Grrr....

This has to be the ugliest solution to this puzzle, but I have little shame in saying I don't care right now. It works and
that'll have to do for now. Some day I will refactor that huge bloated mess of a function. Some day.

I originally tried modelling the circuit but that is unnecessary. I then tried to do it recursively, but blew the stack. There's
probably a way to avoid so much iteration, but like I said, it works.

Note, I simply edited the input file for the second part of the puzzle.

## Day eight
...

## Day nine
This sounded like the travelling salesman and we all know how much fun that is. You'll notice the code is getting uglier
as the puzzles go on. I've given up all pretence that this is anything more that an exercise in getting the correct answer.

Again, a brute force solution to this seems like the only way to solve this one. First, we build a map of locations and
the distances between them. Then using the handy permutations function, we basically get a list of all possible paths through
the locations. It's a simple matter then of iterating each path an calculating its total distance, keeping a track of the
shortest and longest journeys so far.

## Day ten
Another dirty solution.

__Edit__: I read that replacing the call to the list function in the join with a normal comprehension on the
 generator results in a quicker run time. Turns out that the runtime is about half that of the list() version.
 
## Day Thirteen
I'm not keeping my notes up to date!! The past couple of days has just been an exercise in getting the solutions
out as soon as possible.

This one turns out to be a variation of the day nine travelling puzzle. My solution looks similar. Build a mapping
between guests, iterate over all permutation of seating arrangements caclulating the happiness score for each and
return the highest.

The second part simply meant continuing in the score iteration if "me" was one of the guests.

## Day Fourteen
Bad solution. Tried a kind of state machine. Not sure that worked out (certainly not pretty) but got the rigth answer.

__Edit__: I've been looking at other people's solutions. I'm almost too embarrassed to continue. This puzzle has a much
neater mathematical solution which I had no clue about.

I guess there are programmers and then there are hackers !