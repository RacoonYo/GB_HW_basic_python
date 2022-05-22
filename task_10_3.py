class Cell:
    def __init__(self, amount_subcell):
        if amount_subcell > 0:
            self.amount_subcell = amount_subcell
        else:
            raise ValueError(f"Cell can't has {amount_subcell} subcell")

    def __add__(self, other):
        return Cell(self.amount_subcell + other.amount_subcell)

    def __sub__(self, other):
        result = self.amount_subcell - other.amount_subcell
        if result > 0:
            return Cell(result)
        else:
            raise ValueError(f"amount of cell can't be negative. {other.amount_subcell} > {self.amount_subcell}")

    def __mul__(self, other):
        return Cell(self.amount_subcell * other.amount_subcell)

    def __truediv__(self, other):
        return Cell(self.amount_subcell // other.amount_subcell)

    def __floordiv__(self, other):
        return Cell(self.amount_subcell // other.amount_subcell)

    def make_order(self, subcell_in_line):
        return ((('*' * subcell_in_line)+'\n') * (self.amount_subcell // subcell_in_line) +
                '*' * (self.amount_subcell % subcell_in_line))


if __name__ == '__main__':
    first_cell = Cell(18)
    second_cell = Cell(2)

    print((first_cell + second_cell).amount_subcell)
    print((first_cell - second_cell).amount_subcell)
    print((first_cell * second_cell).amount_subcell)
    print((first_cell / second_cell).amount_subcell)
    print((first_cell // second_cell).amount_subcell)
    print(first_cell.make_order(5))
