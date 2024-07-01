from q_learning.action import Action
from q_learning.state import State, StateError
from q_learning.table import RowError, Table


class QTable(Table):
    """Q-table developed by the Agent to choose Actions."""

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
