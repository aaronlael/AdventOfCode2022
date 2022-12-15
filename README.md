# AdventOfCode2022
Repo for Advent of Code 2022 solutions and inputs

Hey, another year to see how far I can get.  Last year, I tried solutions with Go (which I was learning) and Python (which I was familair with).  This year in the interest of my own time, I'll just be doing solutions in Python.

Happy Honda-Days.


Day 1:  The traditional test of "can you use the input" featuring a potential classic off by one indexing error.  It was a good time to figure out how I was going to set up my repo this year.  Last year I jammed all of my inputs into one file but I think this year I'll store all of them in separate files with the test input from the get go to make life "easier". 

Day 2:  I made dictionaries to map the outcomes then parse the input.  I'm sure there was a way that required less thought and manual setup, but it worked the first time performantly which is all I really care about.  Nhawdge will show me the way later.

Day 3:  This felt like an exercise on string slicing based on length and indexing through a list with steps larger than 1.  It was pretty straight forward once I had some coffee in me.  Curse Nhawdge for being a night owl and pulling ahead of me on the private leaderboard.  Curse him.

Day 4:  This one felt like (to me) an excercise in splitting data and using logic to compare values.  It features common errors like incorrect results if you do not cast string representations of numbers to the actual numbers as well as the opportunity to make a very poorly performing solution by actually generated the ranges of numbers like in the example to see if the ranges overlap.

Day 5:  This one took me longer to wrap my night brain around the first half of the input than any other part of the puzzle.  I did some hardcoding I'm not proud of, but it got the job done.  It's also cool to have solved part 2 accidentally by not reading part 1 properly, so I just had to remove a reversing slice operation and I could reuse my entire solution for part 1.  It wasn't difficult but this was my first failed reading comprehension check, which has me concerned.

Day 6:  This was probably one of the easiest days we'll see.  A pretty straight-forward exercise in incrementally parsing through a string looking for a pattern.  I'm sure there are way better ways to do this, but this one works quickly so I'm happy.  Instead of writing a part 2, I just re-wrote part 1 to take an extra input parameter, as it was the style at the time.

Day 7:  This was the first one where I think the test cases were a little "mean" in that you could get the correct answer with grossly wrong code from them.  It took me some time to realize a few mistakes that I was making, mainly that the input data directory structure had the same directory names as subdirectoties of multiple different parent directories.  The I had a very minor math/reading comprehension error at the end of part two that made me question my sanity.  A nice change from day 6.

Day 8:  This is another AoC classic:  the multidimensional-list-look-around type puzzle.  Pretty straight forward except initially I forgot to count the trees that disrupted my viewing pleasure in part two as visible trees, but the test input caught that before I even tried to submit.  All in all a fun puzzle to do while enjoying a cup of coffee and a cinammon roll (or two).

Day 9:  Another AoC classic of navigating space.  It was pretty much like making your own snake game physics.  I used a really cheeky method to handle the diagonals in part one that just did not translate well to part two so I re-wrote it and it was actually a lot simpler than I was making it out to be in my head.  This one took some time, for sure, but it was a nice refresher and didn't have as much hard coding as I suspected it would.

Day 10:  I got part one of this done on Saturday morning and then realized that I had other stuff to do.  This wasn't hard by any means, just annoying.  The end result of my P2 smudged the last letter a tad, but not so much that I couldn't tell what it was.  I'm guessing it has to do with the padding value that I used in part 1 and carried over to P2.

Day 11:  I used classes for this in Python.  Dear god, what have I done.

Day 12:  I started trying to implement A* and then remembered I don't have the attention span to relearn that (even though I implemented it last year on a different puzzle).  I did BFS and it was an instant result for P1 and a tolerable few minutes of run time for P2.  I am not going to optimize it any further because I got the answer and that I what I'm shooting for.

Day 13:  Evil eval.  I spent a lot of time crafting loops and logic to handle sorting this and thankfully it was pretty much all reusable for part 2 after refactoring a bit to work with a list of ordered values for the compairison rather than the pairs provided.

Day 14:  Part 1 was fairly simple.  Build the "container" and then use try/except to find the first instance of sand tripping an index out of range error.  Part two was a little trickier.  I just widended the x axis by the distance from the infinite floor to the sand entry point.  Since that wasn't the max x value already, it made the map sufficiently wide to not throw index errors piling sand on the right.  Yes, I maintained a ton of dead space dots from 0-400 in all of my rows by not using an offset value for the coordinates, but system memory was plentiful.

Day 15:  An optimization problem for me.  I solved P1 but my solution took a while because I looked at all of the points individually.  I was really hoping that P2 wasn't going to expand the way that it did, but it did.  I refactored so that instead of looking at points, I was just looking at ranges of numbers and slicing them into subranges until they were either none left or there was that coveted single coordinate of the mystery beacon.  It wasn't an instant run, but it was less than a few minutes.  As optimal as I'm going to make it.
