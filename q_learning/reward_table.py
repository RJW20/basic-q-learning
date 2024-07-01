from q_learning.action import Action, ActionError
from q_learning.state import State, StateError
from q_learning.table import ColumnError, RowError, Table


class RewardTable(Table):
    """Table of values indicating the reward the Agent receives by making a
    given Action at a given State."""

    def __init__(
        self,
        states_actions_rewards: list[tuple[State, list[tuple[Action, float]]]]
        | None = None,
    ) -> None:
        
        super().__init__()

        if states_actions_rewards:
            for state, actions_and_rewards in states_actions_rewards:
                self.new_rewards(state, actions_and_rewards)

    def new_rewards(
        self,
        state: State,
        actions_and_rewards: list[tuple[Action, float]],
    ) -> None:
        """Create an entry in self for row State with the given Actions and
        corresponding rewards.

        If the row State already exists then raises a StateError.
        """

        try:
            super().new_row(state, actions_and_rewards)
        except RowError:
            raise StateError(
                f"The State {state} already exists in the RewardTable, please "
                + "check your list of States for duplicates."
            )

    def __setitem__(
        self,
        state_action: tuple[State, Action],
        reward: float,
    ) -> None:
        """Set the reward for taking the given Action from the given State.
        
        If the row State doesn't exist then raises a StateError.
        If the action Action doesn't does't exist for the State then raises an
        ActionError.
        """

        try:
            super().__setitem__(state_action, reward)
        except RowError:
            raise StateError(
                f"The State {state_action[0]} does not exist in the "
                + "RewardTable, please check your initial list of States is "
                + "comprehensive."
            )
        except ColumnError:
            raise ActionError(
                f"The State-Action pair {state_action} does not exist in "
                + "the RewardTable, please check your initial list of States "
                + "and Actions is comprehensive."
            )
        
    def __getitem__(self, state_action: tuple[State, Action]) -> float:
        """Get the reward for taking the given Action from the given State.
        
        If the row State doesn't exist then raises a StateError.
        If the action Action doesn't does't exist for the State then raises an
        ActionError.
        """

        try:
            return super().__getitem__(state_action)
        except RowError:
            raise StateError(
                f"The State {state_action[0]} does not exist in the "
                + "RewardTable, please check your initial list of States is "
                + "comprehensive."
            )
        except ColumnError:
            raise ActionError(
                f"The State-Action pair {state_action} does not exist in "
                + "the RewardTable, please check your initial list of States "
                + "and Actions is comprehensive."
            )
