import cmath as c

z = 10 + 5j
print(z)
print(abs(z))  # magnitude of z
print(c.phase(z))

polar = c.polar(z)
print(polar)

rect = c.rect(polar[0], polar[1])
print(rect)
print(rect.real, '+', rect.imag, 'j')
print(c.cos(z))
