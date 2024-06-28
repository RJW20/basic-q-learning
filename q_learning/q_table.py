from q_learning.state import State, StateError
from q_learning.action import Action


class QTable:
    """Q-table developed by the Agent to choose Actions.
    
    Implemented as a dictionary with States as the keys and a list of tuples
    of Actions and their respective Q-value as values.
    """

    def __init__(self, states_and_actions: list[State, list[Action]] | None = None) -> None:

        self.table = dict()
        if states_and_actions:
            for state, actions in states_and_actions:
                self.add_actions(state, actions)

    def add_actions(self, state: State, actions: tuple[Action]) -> None:
        """Create an entry self.table[state] that is a list of tuples of the given 
        actions and the initial value 0.
        
        If self.table[state] already exists throws a StateError.
        """

        if state in self.table:
            raise StateError(f'The State {state} already exists in the QTable, please check your ' + \
                             'list of States for duplicates.')
        
        self.table[state] = [(action, 0) for action in actions]

    def available_actions(self, state: State) -> list[tuple[Action, float]]:
        """Return the list of available Actions and their Q-values at the given State."""
        return self.table[state]