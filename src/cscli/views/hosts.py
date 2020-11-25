
class HostsView():
    def __init__(self, dataset):
        self.dataset = dataset

    def render_table(self, rows):
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

    def render_simple(self):
        rows = []
        for i in self.dataset[0]:
            row = [
                i['hostname'],
                i['os_version'],
                i['agent_version'],
                i['last_seen']
            ]
            rows.append(row)
        self.render_table(rows)
        """
        #col_width = max(len(word) for row in rows for word in row) + 2  # padding
        idx = 0
        col_width = [0, 0, 0, 0]
        for row in rows:
            idx = 0
            for col in row:
                if len(col) > col_width[idx]:
                    col_width[idx] = len(col)
                idx = idx + 1
        print(col_width)
        for row in rows:
            print("".join(
                word.ljust(col_width) for word in row)
            )        for row in rows:
            entry = ""
            for i in range(len(col_width)):
                entry = entry + "{}".format(row[i]).ljust(col_width[i]+2)
            print(entry)
        """
