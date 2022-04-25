# Splitgate_AutoClick

Simple client side hack for the game 'splitgate'.

All it does is read the screen for a red pixel in a spefic location that is part of an indicator to denote that you are aiming at an enemy. When this pixel is red, it sends mouseclick instruction to the game that causes the player to shoot, gauranteeing and hit every time, except for latency, which takes the actual hit rate down to 90%. Getting the latency this low was not so easy however, I had to try many libraries capable of reading the screen and settled on the single one that could read only one pixel instead of the whole screen.
