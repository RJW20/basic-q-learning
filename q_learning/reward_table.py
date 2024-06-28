from q_learning.state import State, StateError
from q_learning.action import Action


class RewardTable:
    """Table of values indicating the reward the Agent receives by making a given
    Action at a given State.
    
    Implemented as dictionary with tuples of States and Actions as the keys and the
    reward as the value.
    """

    def __init__(self, states_actions_rewards: list[tuple[State, Action, float]] | None = None) -> None:

        self.table = dict()
        if states_actions_rewards:
            for state, action, reward in states_actions_rewards:
                self.add_reward(state, action, reward)

    def add_reward(self, state: State, action: Action, reward: float) -> None:
        """Create an entry in self.table with key (state, action) and value reward.
        
        If self.table[(state, action)] already exists throws a StateError.
        """

        if (state, action) in self.table:
            raise StateError(f'The State-Action pair {(state, action)} already exists in the RewardTable, please check your ' + \
                             'list of States and Actions for duplicates.')
        
    def reward_for(self, action: Action, state: State) -> float:
        """Return the reward for taking the given Action at the given State.
        
        If self.table[(state, action)] does not exist throws a StateError.
        """

        try:
            return self.table[(state, action)]
        except KeyError:
            raise StateError(f'The State-Action pair {(state, action)} does not exist in the RewardTable, please check your ' + \
                             'list of States and Actions is comprehensive.')