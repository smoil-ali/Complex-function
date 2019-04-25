from cmath import phase
var=complex(input())
a=var.real
b=var.imag
print(abs(complex(a, b)))
print(phase(complex(a, b)))