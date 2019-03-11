class A:
    def __str__(self):
        return 'A'

    def print_info(self):
        print('A')


class B:
    def __str__(self):
        return 'B'


class C:
    def __str__(self):
        return 'C'

    def get_data(self):
        return 'CData'


class D:
    def __str__(self):
        return 'D'

    def print_info(self):
        print('D')


class E:
    def __str__(self):
        return 'E'

    def print_info(self):
        print('E')


class F(C, D, E):
    def __str__(self):
        return super().__str__() + 'F'

    def get_data(self):
        return super().get_data() + 'FData'

    def print_info(self):
        print('F' + self.get_data())


class G(C, D, E):
    def __str__(self):
        return super().__str__() + 'G'

    def get_data(self):
        return super().get_data() + 'GData'


class H(F, G):
    # class H(G, F):
    def __str__(self):
        return super().__str__() + 'H'

    def print_info(self):
        print('H' + self.get_data())


class J(H):
    def __str__(self):
        return super().__str__() + 'J'


class I(A, J):
    def __str__(self):
        return super().__str__() + 'I'


class X(J, H, B):
    def __str__(self):
        return super().__str__() + 'X'


x = X()
print('print(x):', x)
print('-' * 25)
x.print_info()
