class Action:
    def __init__(self, coordinate, value):
        self.coordinate = coordinate
        self.value = value

    def __repr__(self):
        return '<Action ({}, {})>'.format(self.coordinate, self.value)

    def __eq__(self, other):
        return (self.coordinate == other.coordinate and
                self.value == other.value)
