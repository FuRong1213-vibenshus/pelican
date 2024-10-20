Title: Simple Game by Arcade  
Date: 2024-09-30 09:20
Author: Rong 



## Install the arcade library
+ Refer to [Installation]({filename}/articles/getingstart.md)


## arcade Concepts


1. The **program** determines if the game is over. If so, then the loop ends.
2. The **user input** is processed.
3. The **states** of game objects are updated based on factors such as user input or time.
4. The game displays visuals and plays sound effects based on the new state.

## Game Loops
+ [Using the Window Class](https://learn.arcade.academy/en/latest/chapters/18_window_class/window_class.html)

<details>
  <summary> <b>Arcade Game Skeleton</b> (<i>click to expand</i>)</summary>
  <!-- have to be followed by an empty line! -->


</details>


## Draw items on the screen
+ ***Drawing primitives*** 
    + [Drawing primitivies](https://api.arcade.academy/en/latest/examples/index.html#sprite-player-movement)
+ ***Animations***
    + [Bouncing Shapes](https://api.arcade.academy/en/latest/examples/shapes.html#shapes-slow)
+ ***Sprites***
    + [Sprites](https://api.arcade.academy/en/latest/examples/sprite_collect_coins.html#sprite-collect-coins)

## Manage on-screen graphic elements
### Sprite and Sprite List
+ [Sprites And Collisions](https://learn.arcade.academy/en/latest/chapters/21_sprites_and_collisions/sprites.html)
+ [Moving Sprites](https://learn.arcade.academy/en/latest/chapters/22_moving_sprites/moving_sprites.html)




### Exercise 
1. Download the whole folder [alien_invasion](https://github.com/FuRong1213-vibenshus/arcade/tree/main/alien_invasion) from github. Put it into the same arcade virtual environment and run.
2. Make the bullets(laser) move forward. 
3. (Optional) Make the bullets(laser) move randomly.
4. (Optional) Make the aliens move randomly.  
5. (Optional) Make the aliens also shoot.  

## Handle user input

### Exercise
1. Make some of bullets move quicker than others, depends on which key the player presses -- they are the more powerful bullets. 
2. (Optional) Give a limited number to the powerful bullets, display them to the window. 
3. (Optional) Collision detects between myship and the aliens. It cost one life if it happens.  

## Play sound effects and music

