from q_learning.action import Action, ActionError
from q_learning.state import State, StateError
from q_learning.table import ColumnError, RowError, Table


class QTable(Table):
    """Q-table used by the Agent to choose Actions.
    
    Develops over time to improve its entries to enable the Agent to choose
    better Actions.
    """

    def __init__(
        self,
        states_and_actions: list[tuple[State, list[Action]]] | None = None,
    ) -> None:

        super().__init__()

        if states_and_actions:
            for state, actions in states_and_actions:
                self.new_actions(state, actions)

    def new_actions(self, state: State, actions: list[Action]) -> None:
        """Create an entry in self for the row State with the given Actions and
        the initial values 0.
        
        If the row State already exists then raises a StateError.
        """

        actions_and_initials = [(action, 0) for action in actions]

        try:
            super().new_row(state, actions_and_initials)
        except RowError:
            raise StateError(
                f"The State {state} already exists in the QTable, please "
                + "check your list of States for duplicates."
            )

    def best_action(self, state: State) -> tuple[Action, float]:
        """Return the Action and its Q-value for the Action with highest Q-value
        in the row State.
        
        If the row State doesn't exist then raises a StateError.
        """

        try:
            actions = super().get_row(state)
            best_action = max(actions, key=actions.get)
            return best_action, actions[best_action]
        except RowError:
            raise StateError(
                f"The State {state} does not exist in the QTable, please "
                + "check your initial list of States is comprehensive."
            )
        
    def __setitem__(self, state: State, action: Action, q_value: float) -> None:
        """Set the q_value associateed with the given Action at the given State.
        
        If the row State doesn't exist then raises a StateError.
        If the action Action doesn't does't exist for the State then raises an
        ActionError.
        """

        try:
            super.__setitem__(state, action, q_value)
        except RowError:
            raise StateError(
                f"The State {state} does not exist in the QTable, please "
                + "check your initial list of States is comprehensive."
            )
        except ColumnError:
            raise ActionError(
                f"The State-Action pair {(state, action)} does not exist in "
                + "the QTable, please check your initial list of States "
                + "and Actions is comprehensive."
            )
        
    def __getitem__(self, state: State, action: Action) -> float:
        """Get the Q-value associated with the given Action at the given State.
        
        If the row State doesn't exist then raises a StateError.
        If the action Action doesn't does't exist for the State then raises an
        ActionError.
        """

        try:
            return super.__getitem__(state, action)
        except RowError:
            raise StateError(
                f"The State {state} does not exist in the QTable, please "
                + "check your initial list of States is comprehensive."
            )
        except ColumnError:
            raise ActionError(
                f"The State-Action pair {(state, action)} does not exist in "
                + "the QTable, please check your initial list of States "
                + "and Actions is comprehensive."
            )

    def update(
        self,
        state: State,
        action: Action,
        reward: float,
        learning_rate: float,
        discount_factor: float,
        next_best_q: float,
    ) -> None:
        """Update the Q-value in self at the given State, Action."""

        self[state, action] = (1 - learning_rate) * self[state, action] + \
            learning_rate * (reward +  discount_factor * next_best_q)
