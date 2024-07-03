# Basic Q-Learning
Implementation of basic Q-learning with a Q-table, written in Python.

## How it Works

### Setup
The Agent has access to both a QTable and a RewardTable. These contain values for every State and possible Action available at those States, and are implemented as nested dictionaries for efficient value retrieval. Note that every Action takes one State and returns a different State.

### Movement
To navigate its environment, at every timestep, the agent looks in the QTable for the Q-values associated with the Actions available in its current State and chooses and carries out the Action that has the highest.

### Learning
To optimize the QTable, after choosing but before carrying out an Action, the QTable value for the previous State and Action is updated using the formula:

&nbsp; &nbsp; &nbsp; $Q^{new}(S_{prev},A_{prev}) = (1 - \alpha) \cdot Q^{old}(S_{prev},A_{prev}) + \alpha \cdot (R_{prev} + \gamma \cdot q_{curr})$

where:
- $R_{prev}$ is the value in the RewardTable at $(S_{prev},A_{prev})$.
- $q_{curr}$ is the Q-value associated with the Action the Agent is about to take in its current State.
- $\alpha$ is the learning rate.
- $\gamma$ is the discount factor.

Both these last two hyperparameters are chosen before training, for more information on how changing them affects the learning see [here](https://en.wikipedia.org/wiki/Q-learning#Influence_of_variables).

## Usage

### States and Actions
- Each State must be a unique state of the environment, able to be represented by a unique (hashable) identifier e.g. a tuple representing the grid position in 2D space.
- Each Action must be intiated with a unique function that takes one State and returns another e.g. taking the tuple $(x, y)$ to $(x + 1,y)$.

### QTable and RewardTable
- The QTable requires a list of States matched up with all their available Actions.
- The RewardTable requires a list of States matched up with all their available Actions paired with the reward gained for taking that Action from the State.

### Settings
Set the value of $\alpha$ and $\gamma$.

### Agent
Initialise the agent with the State that represents the position the Agent starts in, QTable, RewardTable, learning rate $\alpha$ and discount factor $\gamma$. Then make repeated calls to `agent.next_state()`.

## Examples
- [Mouse and Cheese](https://github.com/RJW20/basic-q-learning/tree/main/mouse_and_cheese)
