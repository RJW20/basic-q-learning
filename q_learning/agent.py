from q_learning.action import Action, ActionError
from q_learning.q_table import QTable
from q_learning.reward_table import RewardTable
from q_learning.state import State


class Agent:
    """Agent in the environment."""

    def __init__(
        self,
        starting_state: State,
        reward_table: RewardTable,
        q_table: QTable,
        learning_rate: float,
        discount_factor: float,
    ) -> None:
        
        self.starting_state = starting_state

        self.current_state: State = starting_state
        self.previous_state: State | None = None
        self.previous_action: Action
        self.previous_reward: float

        self.reward_table: RewardTable = reward_table
        self.q_table: QTable = q_table

        self.learning_rate: float = learning_rate
        self.discount_rate: float = discount_factor

    def reset(self) -> None:
        """Return the Agent to the starting State."""

        self.current_state = self.starting_state
        self.previous_state = None

    def next_state(self) -> None:
        """Choose and perform an Action using self.q_table.
        
        Resets the agent if no Actions are available.
        Updates the Q-value for the previous state before advancing.
        """

        try:

            action, q = self.q_table.best_action(self.current_state)

            if self.previous_state:
                self.q_table.update(
                    self.previous_state,
                    self.previous_action,
                    self.previous_reward,
                    self.learning_rate,
                    self.discount_rate,
                    q,
                )

            self.previous_state = self.current_state
            self.previous_action = action
            self.previous_reward = self.reward_table[self.current_state, action]
            self.current_state = action.act_on(self.current_state)

        except ActionError:
            
            if self.previous_state:
                self.q_table.update(
                    self.previous_state,
                    self.previous_action,
                    self.previous_reward,
                    self.learning_rate,
                    self.discount_rate,
                    0,
                )

            self.reset()
