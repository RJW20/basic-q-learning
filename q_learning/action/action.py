from typing import Callable, Hashable

from q_learning.state import State


class Action:
    """Unique Action in the Agent's environment."""

    def __init__(self, effect_on_state: Callable[[Hashable], Hashable]) -> None:
        self._effect_on_state: Callable[[Hashable], Hashable] = effect_on_state

    def act_on(self, state: State) -> State:
        """Return the State achieved by taking this Action from the given
        State."""
        return State(self._effect_on_state(state._identifier))

    def __hash__(self) -> int:
        """Return the hash of this Action effect function."""
        return hash(self._effect_on_state)
