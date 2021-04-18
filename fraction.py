
class Fraction():
    def __init__(self, top, bottom):
        if not isinstance(top, int) or not isinstance(bottom, int):
            raise 'Not a int'
        common = self.gcd(top,bottom)
        self.num = top//common
        self.den = bottom//common


    def __str__(self):
        return f"{self.num} / {self.den}"

    def __add__(self, the_other_fraction):
        new_num = self.num*the_other_fraction.den + self.den*the_other_fraction.num
        new_den = self.den * the_other_fraction.den
        return Fraction(new_num, new_den)

    def __sub__(self, the_other_fraction):
        new_num = self.num*the_other_fraction.den - self.den*the_other_fraction.num
        new_den = self.den * the_other_fraction.den
        return Fraction(new_num, new_den)

    def __mul__(self, the_other_fraction):
        new_num = self.num*the_other_fraction.num
        new_den = self.den*the_other_fraction.den
        common = self.gcd(new_num, new_den)
        return Fraction(new_num//common, new_den//common)

    def __truediv__(self, the_other_fraction):
        new_num = self.num * the_other_fraction.den
        new_den = self.den * the_other_fraction.num
        common = self.gcd(new_num, new_den)
        return Fraction(new_num//common, new_den//common)

    def __eq__(self, the_other_fraction):
        if self.num == the_other_fraction.num and self.den == the_other_fraction.den:
            return True
        else:
            return False

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def gcd(self, m, n):
        """
        Euclid's algorithm

        :param m:
        :param n:
        :return:
        """
        while m%n != 0:
            old_m = m
            old_n = n

            m = old_n
            n = old_m % old_n
        return n




if __name__ == "__main__":
    myfraction=Fraction(1,4)
    print(myfraction)
    print(myfraction + Fraction(1,2)) # .25 + .5 = 0.75 --> 3/4
    print(myfraction - Fraction(1,2)) # .25 - .5 = -.25 --> -1/4
    print(myfraction * Fraction(2,4))
    print(myfraction / Fraction(1,2)) # 1/4 / 1/2 --> 1/2
    print(Fraction(1.4, 2))
    print(Fraction(1,4) == Fraction(1,4))