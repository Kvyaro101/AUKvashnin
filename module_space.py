"""Модуль, который описывает алгебру модулей"""
from numbers import Number

class ModuleValueError(ValueError):
    """Auxiliary class to definy name ModuleValueError and get more points in Pylint"""

ModuleValue = 7

class ModuleRemainder:
    """Class of modulo remainders"""
    def __init__(self,arg=0):
        """coefficient – значение в кольце остатков по модулю"""
        if isinstance(arg, int):
            self.coefficient = arg % ModuleValue
        else:
            raise ModuleValueError("You're trying to get module from" + repr(arg))

    @staticmethod
    def nothing(self):
        """Method that do nothing but help to avoid arg error in next methods"""

    def __str__(self):
        """Method that multiply modules"""
        return str(self.coefficient)

    def __eq__(self, other):
        """Method that checks modules for equality"""
        if isinstance(other, int):
            other = ModuleRemainder(other)
            return self.coefficient == other.coefficient
        else:
            raise ModuleValueError(
        "Can't assert if Module remainder is equal to " + str(type(other)))

    def __add__(self, other):
        """Method that sum modules"""
        if isinstance(other, int):
            other = ModuleRemainder(other)
        elif isinstance(other, ModuleRemainder):
            pass
        else:
            raise ModuleValueError(f"Unexpeted data type, {str(type(other))} given, not int")
        return ModuleRemainder(self.coefficient+other.coefficient % ModuleValue)

    def __radd__(self, other):
        return self.__add__(other)

    def __neg__(self):
        return ModuleRemainder(-self.coefficient)

    def __sub__(self, other):
        if isinstance(other, Number):
            other = ModuleRemainder(other)

        return self.__add__(other.__neg__())

    def __rsub__(self, other):
        return self.__neg__().__add__(other)

    def __mul__(self, other):
        if isinstance(other, Number):
            other = ModuleRemainder(other)
        elif isinstance(other, ModuleRemainder):
            pass
        else:
            raise ModuleValueError(f"Unexpeted data type, {str(type(other))} given, not int")
        return ModuleRemainder((self.coefficient * other.coefficient) % ModuleValue)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __divmod__(self, other):
        if isinstance(other, Number):
            other = ModuleRemainder(other)
        elif isinstance(other, ModuleRemainder):
            pass
        else:
            raise ModuleValueError(f"Unexpeted data type, {str(type(other))} given, not int")
        return ModuleRemainder((self.coefficient//other.coefficient)), ModuleRemainder(
            (self.coefficient%other.coefficient))

    def __floordiv__(self, other):
        return divmod(self, other)[0] #Как удобно, однако

    def __mod__(self, other):
        return divmod(self, other)[1]

    def __rfloordiv__(self, other):
        return divmod(other, self)[0]

    def __rmod__(self, other):
        return divmod(other, self)[1]

    def __rdivmod__(self, other):
        return ModuleRemainder(other).__divmod__(self)

    def __complex__(self):
        """Transform module to complex number"""
        return complex(self.coefficient)

    def __float__(self):
        """Transform module to float number"""
        return float(self.coefficient)

    def __int__(self):
        """Transform module to integer number"""
        return int(self.coefficient)

m1 = ModuleRemainder()
m2 = ModuleRemainder(5)
m3 = ModuleRemainder(-8)

print(m2+m3,m2+3,m2==3,m2*m3,m3*2,m2%m3,m3//m2,complex(m1),float(m2),int(m3))
