# Python Video Poker Simulator

Messing around trying to create a program to run simulations for various types of video poker.

Ideally will be able to get distribution of outcomes of playing
different games for *X* hands using different strategies (for now only care about realistic "human" optimal strats)

Once this is accomplished want to be able to run simulations involving *n* hands.

## Methodology
Currently the plan is to come up with various ways to cut down on the various hold/discard combinations when evaluating the estimated value of each hold possiblity. 

--
## Brute Force Method
Turns out python is slow as mud. Need to optimize. 

Was able to reduce evaluating a random hand from ~30seconds on local MacBook Pro using brute_force.py down to ~3seconds. This still isn't fast enough for multiple 1MM+ hand simulations.

## Testing
To run current tests, in project directory run command: nose2
