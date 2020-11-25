class Worker:

    def __init__(self, n, s, p, wage, bonus):
        self.name = n
        self.surname = s
        self.position = p
        self._income = {"wage": int(wage), "bonus": int(bonus)}

class Position(Worker):

    def __init__(self, n, s, p, wage, bonus):
        super().__init__(n, s, p, wage, bonus)

    def get_full_name(self):
       print(f"{self.name} {self.surname}")

    def get_total_income(self):
        print(self._income["wage"]+self._income["bonus"])


par = Position("Vika", "Busygina", "IT", 40000, 40000)
par.get_full_name()
par.get_total_income()


