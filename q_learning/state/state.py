from typing import Hashable

from q_learning.state.state_error import StateError


class State:
    """Unique State in the Agent's environment."""

    def __init__(self, identifier: Hashable) -> None:
        self._identifier: Hashable = identifier

        # Test that this State is valid
        try:
            self.__hash__()
        except TypeError:
            raise StateError(f"Unable to instatiate State with identifier {identifier} as it is not hashable.")

    def __hash__(self) -> int:
        """Return the hash of this States identifier."""
        return hash(self._identifier)
