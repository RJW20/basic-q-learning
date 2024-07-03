# Mouse and Cheese
An application of basic Q-learning with a Q-table applied to the canonical example of a mouse seeking out cheese in a maze.

## Setup

### States
The States are represented by tuples representing 2D grid points.

### Actions
- The Actions contain functions that add 1 or take 1 from one value in the States' 2D grid points. These correspond to the Mouse (the Agent) moving up, right, down or left.
- Actions are only in the Tables if they take a State to another valid State.
- States where an episode is over (on the same tile as a Cat or Cheese) have no available Actions, so the Agent knows to reset.

### Rewards
The Mouse earns a reward of 100 for reaching the Cheese but a reward of -10 for hitting a Cat.

## Result
The Mouse is able to reach the Cheese efficiently given any (solvable) arrangement of Cats and Cheese given enough time. Below is one such example:

![mouse_find_cheese](https://github.com/RJW20/basic-q-learning/assets/99192767/a29511be-1ddb-4d97-9070-80bb9fff414a)
