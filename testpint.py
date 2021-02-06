import pint

units = pint.UnitRegistry()

a = 10 * units.inches
b = 23 * units.cm
c = a + b

print(c.to(units.meters))