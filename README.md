# Poker Game

I wasn't really sure how I would test the program and that's when I realized that the player cards were supposed to be passed into the function, as opposed to being randomly generated inside my `poker_game()` function. Nonetheless, I hope the program is similar enough to how it should be.

NOTE: Normally JavaScript is my best language, but I decided to use Python because I figured coding a terminal game would be easier in Python rather than in JavaScript.

- No dependencies!
- I don't think the instructions mentioned what to do if a key other than `H` or `S` are pressed. So, I decided to print a message asking the user to try again. Originally, hitting any key besides `H` would result in a stand.
- As far as I can tell the the poker game is working well and is without bugs. The `poker_game()` function is a bit long so I hope the comments make it easier to undersand.
- I kept things pretty simple. Two functions for helping calculate a card or hand value and one main function. The only data structures that I used were arrays.
- Since this was a pretty simple application mostly made up of if statements and loops, I wasn't worried about speed and didn't have to make tradeoffs while coding.
- If I had more time, then I would implement the program so that the player cards are passed in and not randomly generated. This would allow me to properly test the program.
- I was constantly running my program as I was working through it to make sure it was working as expected.
- To run the tests, you can run: `python test_poker.py`. These tests are very basic.
