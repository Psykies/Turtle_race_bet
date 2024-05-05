# Turtle Race Betting Game

This Python script simulates a turtle race betting game where users can choose a turtle color and place a bet on which turtle will win the race.

## Description

The script creates a turtle race game where turtles of different colors compete in a race. Users are prompted to choose a color and place a bet on the winning turtle. Once the race starts, the turtles move forward randomly, and the first turtle to reach the finish line wins the race. The script then announces the winner and informs the user whether they have won or lost their bet.

## Modules Used

- `turtle`: Provides a graphical environment for creating drawings and animations.
- `random`: Allows for generating random numbers used to determine turtle movement.

## Functions Used

- `screen.textinput(title, prompt)`: Prompts the user with a title and a message and waits for the user to enter some text. Returns the text entered by the user.
- `Turtle()`: Creates a new turtle object.
- `turtle.penup()`: Lifts the pen, so the turtle does not draw while moving.
- `turtle.color(color)`: Sets the color of the turtle's pen.
- `turtle.goto(x, y)`: Moves the turtle to the specified coordinates.
- `turtle.xcor()`: Returns the current x-coordinate of the turtle.
- `turtle.pencolor()`: Returns the color of the turtle's pen.
- `turtle.forward(distance)`: Moves the turtle forward by the specified distance.
- `random.randint(a, b)`: Returns a random integer between a and b, inclusive.

## Usage

1. Ensure you have Python installed on your system.
2. Clone or download the repository containing the script.
3. Run the script using a Python interpreter.

## Instructions

1. Upon running the script, a window will open displaying the turtle race game.

2. Choose a color to bet on:
   - Options: red, green, yellow, blue, orange, or purple.
   - Enter your bet when prompted.

3. Watch as the turtles race towards the finish line.

4. Once a turtle wins the race, the script will announce the winner and inform you whether you have won or lost your bet.

5. Close the window to exit the game.

## Example

```python
print (f"you have won! The {winning_color} turtle is the winner")
```

Replace `{winning_color}` with the color of the winning turtle.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

