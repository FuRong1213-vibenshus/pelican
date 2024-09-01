Title: Simple Game by Arcade  
Date: 2024-08-31 09:20
Author: Rong 


## Background

**It is highly recommended that
you read the relevant parts of the articles below along the whole process,
however some of the functions mentioned in the articles are obsolete**

+ [Arcade: A Primer on the Python Game Framework](https://realpython.com/arcade-python-game-framework/)
+ [Build a Platform Game in Python With Arcade](https://realpython.com/platformer-python-arcade/)


## Install the arcade library
+ Refer to [Installation]({filename}/articles/getingstart.md)

## Draw items on the screen
+ ***Drawing primitives*** 
    + [Drawing primitivies](https://api.arcade.academy/en/latest/examples/index.html#sprite-player-movement)

+ ***Animations***
    + [Bouncing Shapes](https://api.arcade.academy/en/latest/examples/shapes.html#shapes-slow)

+ ***Sprites***
    + [Sprites](https://api.arcade.academy/en/latest/examples/sprite_collect_coins.html#sprite-collect-coins)


## Work with the arcade Python game loop

1. The **program** determines if the game is over. If so, then the loop ends.
2. The **user input** is processed.
3. The **states** of game objects are updated based on factors such as user input or time.
4. The game displays visuals and plays sound effects based on the new state.

<details>
  <summary> <b>Arcade Game Skeleton</b> (<i>click to expand</i>)</summary>
  <!-- have to be followed by an empty line! -->

```
import arcade
class MyGame(arcade.Window):

    def __init__(self):

        pass

    def setup(self):

        """
        Sets up the game for the current level
        """
        pass

    def on_key_press(self, key: int, modifiers: int):

        """
        Processes key presses
        Arguments:
            key {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were down at the time
        """

    def on_key_release(self, key: int, modifiers: int):
        """
        Processes key releases
        Arguments:
            key {int} -- Which key was released
            modifiers {int} -- Which modifiers were down at the time
        """

    def on_update(self, delta_time: float):

        """
        Updates the position of all game objects
        Arguments:
            delta_time {float} -- How much time since the last call
        """
        pass

    def on_draw(self):
        pass


if __name__ == "__main__":
    window = Platformer()
    window.setup()
    arcade.run()
```

</details>


## Manage on-screen graphic elements



## Handle user input

## Play sound effects and music

