from .view import IView

class HostsView(IView):
    def __init__(self, dataset):
        self.dataset = dataset

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
        self._render_table(rows)
