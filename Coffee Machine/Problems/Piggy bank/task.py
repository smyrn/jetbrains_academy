class PiggyBank:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars
        self.cents += deposit_cents

        if self.cents > 99:
            whole_dollars = self.cents // 100
            self.dollars += whole_dollars
            self.cents -= whole_dollars * 100
