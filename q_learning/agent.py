from q_learning.action import Action
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
        discount_rate: float,
    ) -> None:

        self.current_state: State = starting_state
        self.previous_state: State | None = None
        self.previous_action: Action
        self.previous_reward: float

        self.reward_table: RewardTable = reward_table
        self.q_table: QTable = q_table

        self.learning_rate: float = learning_rate
        self.discount_rate: float = discount_rate

    def next_state(self) -> None:
        """Choose and perform an Action using self.q_table.
        
        Updates the Q-value for the previous state before advancing.
        """

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
