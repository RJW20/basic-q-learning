from typing import Any, Hashable

from q_learning.table.errors import ColumnError, RowError


class Table(dict):
    """ "2D array with O(1) look up time.

    Implemented as a dictionary of dictionaries.
    """

    def new_row(
        self,
        row_label: Hashable,
        row: list[tuple[Hashable, Any]],
    ) -> None:
        """Add a new row entry.

        If the row already exists then raises a RowError.
        """

        try:
            super().__getitem__(row_label)
            raise RowError(f"Row {row_label} already exists in the Table.")
        except KeyError:
            super().__setitem__(
                row_label,
                {column_label: value for column_label, value in row},
            )

    def get_row(self, row_label: Hashable) -> dict[Hashable, Any]:
        """Return the row with given row_label.

        If the row doesn't exist then raises a RowError.
        """

        try:
            return super().__getitem__(row_label)
        except KeyError:
            raise RowError(f"Row {row_label} does not exist in the Table.")

    def get_element_at(
        self,
        row_label: Hashable,
        column_label: Hashable
    ) -> Any:
        """Return the value in row row_label in position column_label.

        If the row doesn't exist then raises a RowError.
        If the column doesn't exist within the row then raises a ColumnError.
        """

        try:
            self.get_row(row_label)
            return row_label[column_label]
        except KeyError:
            raise ColumnError(
                f"Column {column_label} does not have a value in the row "
                + "{row_label}."
            )
