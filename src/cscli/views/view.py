from abc import ABC
from abc import abstractmethod


class IView(ABC):
    """Base view abstract class with view rendering functions"""
    def _render_table(self, rows):
        """Render table will take in a list of rows and render with
        adjusted column width based on the longest row entries."""
        idx = 0
        col_width = []

        try:
            for i in range(len(rows[0])):
                col_width.append(0)
        except IndexError:
            return

        for row in rows:
            idx = 0
            for col in row:
                if len(col) > col_width[idx]:
                    col_width[idx] = len(col)
                idx = idx + 1

        for row in rows:
            entry = ""
            for i in range(len(col_width)):
                entry = entry + "{}".format(row[i]).ljust(col_width[i]+2)
            print(entry) 