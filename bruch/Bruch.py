"""This module includes a Bruch class."""


class Bruch(object):
    """Bruch is a class to  represent mathematical fractions."""

    def __iter__(self):
        """
        Get iterator for iterating trough the numerator and the denominator.

        :return: the iterator of the tuple containing the numerator and the denominator
        """
        return (self.zaehler, self.nenner).__iter__()

    def __init__(self, zaehler, nenner=1):
        """
        Constructs fraction from a number or numerator and denominator.

        :param zaehler(``Bruch,int``): the numerator or a fraction
        :param nenner(``int``): the denominator (default = 1)
        :raises:
            ZeroDivisionError: if the denominator is 0
        :raises:
            TypeError: if the given argument is not a fraction
            or the given arguments are not two ints
        """
        if isinstance(zaehler, Bruch):
            self.zaehler = zaehler.zaehler
            self.nenner = zaehler.nenner
        elif isinstance(zaehler, int) and isinstance(nenner, int):
            if nenner == 0:
                raise ZeroDivisionError()
            else:
                self.zaehler = zaehler
                self.nenner = nenner
        else:
            raise TypeError()
        self.__normalize()

    def __float__(self):
        """
        Get float representation of the fraction.

        :return: float of fraction
        """
        return float(self.zaehler) / float(self.nenner)

    def __abs__(self):
        """
        Get the absolute of this fraction.

        :return: a positive copy of the fraction
        """
        return Bruch(abs(self.zaehler), abs(self.nenner))

    def __eq__(self, other):
        """
        Checks if the fraction is equal to another value.

        :param other(``Bruch,int,float``): the other value
        :return: if the two values are equal
        """
        return float(self) == float(other)

    def __int__(self):
        """
        Gets an integer representation of the fraction.

        :return: int representation
        """
        return self.zaehler // self.nenner

    def __invert__(self):
        """
        Changes numerator and denominator.

        :return: inverted fraction
        """
        return Bruch(self.nenner, self.zaehler)

    def __str__(self):
        """
        String representation of the fraction.

        :return: string representation in the form of (x/x) or (x) if the denominator is 1
        """
        if self.nenner == 1:
            return "(" + str(self.zaehler) + ")"
        else:
            return "(" + str(self.zaehler) + "/" + str(self.nenner) + ")"

    def __pow__(self, power):
        """
        Raises the fraction to the power of the argument power.
        This is done by raising the numerator
        and the denominator to the power of the argument power.

        :param power: the exponent
        :return: result of fraction to the power of argument power
        """
        return Bruch(self.zaehler ** power, self.nenner ** power)

    def __neg__(self):
        """
        Negates the fraction by negating the numerator.

        :return: negated copy of the fraction
        """
        return Bruch(-self.zaehler, self.nenner)

    def __ge__(self, other):
        """
        Checks if the fraction is greater than or equal to another value.

        :param other(``int,float,Bruch``): the value to compare to
        :return: if the fraction is greater or equal
        """
        return float(self) >= float(other)

    def __gt__(self, other):
        """
         Checks if the fraction is greater than another value.

        :param other(``int,float,Bruch``): the value to compare to
        :return: if the fraction is greater
        """
        return float(self) > float(other)

    def __lt__(self, other):
        """
         Checks if the fraction is less than another value.

        :param other(``int,float,Bruch``): the value to compare to
        :return: if the fraction is less
        """
        return float(self) < float(other)

    def __le__(self, other):
        """
        Checks if the fraction is less than or equal to another value.

        :param other(``int,float,Bruch``): the value to compare to
        :return: if the fraction is less or equal
        """
        return float(self) <= float(other)

    def __ne__(self, other):
        """
        Checks if the fraction is not equal to another value.

        :param other(``Bruch,int,float``): the other value
        :return: if the two values are not equal
        """
        return float(self) != float(other)

    def __normalize(self):
        """
        Makes the denominator positive.

        :return: the fraction with a positive denominator
        """
        if self.nenner < 0:
            self.zaehler = -self.zaehler
            self.nenner = -self.nenner

    def __add__(self, other):
        """
        Adds the fraction and the other value.

        :param other(``int,Bruch``): value to add
        :return: the sum
        """
        other = Bruch(other)
        return Bruch(self.zaehler * other.nenner + other.zaehler * self.nenner,
                     self.nenner * other.nenner)

    def __iadd__(self, other):
        """
        Adds the other value to the fraction.

        :param other(``int,Bruch``): value to add
        :return: the sum
        """
        # noinspection PyMethodFirstArgAssignment
        self = self + other
        return self

    def __radd__(self, other):
        """
        Adds the fraction and the other value.

        :param other(``int,Bruch``): value to add
        :return: the sum
        """
        return self + other

    def __sub__(self, other):
        """
        Subtracts the other value from the fraction.

        :param other(``int,Bruch``): the other value
        :return: difference
        """
        return self + -other

    def __isub__(self, other):
        """
        Subtracts the other value from the fraction and saves the result.

        :param other(``int,Bruch``): the other value
        :return: difference
        """
        # noinspection PyMethodFirstArgAssignment
        self = self - other
        return self

    def __rsub__(self, other):
        """
        Subtracts the fraction from the other value.

        :param other(``int,Bruch``): the other value
        :return: difference
        """
        return Bruch(other) - self

    def __mul__(self, other):
        """
        Multiplies a fraction with another value.

        :param other(``int,Bruch``): the other value
        :return: product
        """
        other = Bruch(other)
        return Bruch(self.zaehler * other.zaehler, self.nenner * other.nenner)

    def __imul__(self, other):
        """
        Multiplies a fraction with another value and saves the new fraction.

        :param other(``int,Bruch``): the other value
        :return: product
        """
        # noinspection PyMethodFirstArgAssignment
        self = self * other
        return self

    def __rmul__(self, other):
        """
        Multiplies a fraction with another value.

        :param other(``int,Bruch``): the other value
        :return: product
        """
        return self * other

    def __truediv__(self, other):
        """
        Divides a fraction by another value.

        :param other(``int,Bruch``): the divisor
        :return: the quotient
        """
        return self * ~Bruch(other)

    def __itruediv__(self, other):
        """
        Divides a fraction by another value and saves it.

        :param other(``int,Bruch``): the divisor
        :return: the quotient
        """
        # noinspection PyMethodFirstArgAssignment
        self = self / other
        return self

    def __rtruediv__(self, other):
        """
        Divides the other value by the fraction.

        :param other(``int,Bruch``): the dividend
        :return: the quotient
        """
        return Bruch(other) / self

    # noinspection PyPep8Naming
    @classmethod
    def __makeBruch(cls, value):
        """
        Another way to call the constructor. Returns an instance of the Bruch class.

        :param value(``int,Bruch``): the fraction's value
        :return: an instance of the Bruch class
        """
        return Bruch(value)
