class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real_part = real
        self.imaginary_part = imaginary

    def display(self):
        if self.imaginary_part >= 0:
            print(f"{self.real_part} + {self.imaginary_part}i")
        else:
            print(f"{self.real_part} - {-self.imaginary_part}i")

c1 = ComplexNumber(3, 2)
c2 = ComplexNumber(1, -7)

c1.display()
c2.display()
