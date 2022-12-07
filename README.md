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
