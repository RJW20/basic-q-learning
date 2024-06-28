from q_learning.state import State
from q_learning.reward_table import RewardTable
from q_learning.q_table import QTable


class Agent:
    """Agent in the environment."""

    def __init__(
        self,
        starting_state: State,
        reward_table: RewardTable,
        q_table: QTable,
    ) -> None:

        self.state: State = starting_state
        self.reward_table: RewardTable = reward_table
        self.q_table: QTable = q_table

    def next_state(self) -> None:
        """Choose and perform an Action using self.q_table.
        
        Updates self.q_table based on the reward received for taking the Action 
        as found in self.reward_table.
        """