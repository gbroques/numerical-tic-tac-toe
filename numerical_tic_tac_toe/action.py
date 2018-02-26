class Action:
    def __init__(self, coordinate, number):
        self.coordinate = coordinate
        self.number = number

    def __repr__(self):
        return '<Action ({}, {})>'.format(self.coordinate, self.number)

    def __eq__(self, other):
        return (self.coordinate == other.coordinate and
                self.number == other.number)
