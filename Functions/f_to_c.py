


def conc_f_to_c(f):
    c = round((f - 32) * 5.0 / 9.0)
    return c

print(conc_f_to_c(212))
print(conc_f_to_c(90))
print(conc_f_to_c(72))
print(conc_f_to_c(32))
print(conc_f_to_c(0))
print(conc_f_to_c(-40))