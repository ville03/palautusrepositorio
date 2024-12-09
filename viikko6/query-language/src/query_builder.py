from matchers import All, And, Or, Not, HasAtLeast, HasFewerThan, PlaysIn

class QueryBuilder:
    def __init__(self):
        self.query = All()

    def build(self):
        query = self.query
        self.query = All()
        return query
    
    def plays_in(self, team):
        self.query = And(PlaysIn(team), self.query)
        return self
    
    def has_at_least(self, value, attr):
        self.query = And(HasAtLeast(value, attr), self.query)
        return self
    
    def has_fewer_than(self, value, attr):
        self.query = And(HasFewerThan(value, attr), self.query)
        return self
    
    def one_of(self, *matchers):
        self.query = Or(*matchers)
        return self

    
#matcher = And(
#    HasAtLeast(70, "points"),
#    Or(
#        PlaysIn("NYR"),
#        PlaysIn("FLA"),
#        PlaysIn("BOS")
#    )
#)