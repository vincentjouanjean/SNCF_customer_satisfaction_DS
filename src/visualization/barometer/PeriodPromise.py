class PeriodPromise:
    def __init__(self, title, _global, p1, p2, p3, p4, p5, p6, p7):
        # Add period index, they are different depending on the files
        self.fields = ['_global', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7']
        self.title = title
        self._global = _global
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.p5 = p5
        self.p6 = p6
        self.p7 = p7
