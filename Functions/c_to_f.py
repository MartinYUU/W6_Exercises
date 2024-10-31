def conv_c_to_f(c):
    f = round((c * 9.0 / 5.0) + 32)
    return f

print(conv_c_to_f(100))
print(conv_c_to_f(45))
print(conv_c_to_f(19))
print(conv_c_to_f(0))
print(conv_c_to_f(-7))
print(conv_c_to_f(-40))