# ∗ get_soc_sec_tax() : accepts a gross pay amount and returns the Social Security tax 
# on that amount. Assume a tax rate of 6.2% 
# ∗ get_medicare_tax() : accepts a gross pay amount and returns the Medicare tax on 
# that amount. Assume a tax rate of 1.45%

#  get_federal_tax() : accepts a gross pay amount and withholding code, and returns 
# the federal tax withholding on that amount. Use the tax table below. (You will need 
# to use an if / else statement. The case for withholding code 4+ is extra tricky!) 
# Withholding Code    Tax Rate 
# 0                   23% 
# 1                   21% 
# 2                   19.5% 
# 3                   18.5% 
# 4+                  18% less 0.5% for each withholding over 4 
# (ex, code 6: rate .18 – (2 x .005) = .17 (or 17%)

def get_soc_sec_tax(gpay):
    return gpay * 0.062

def get_medicare_tax(gpay):
    return gpay * 0.0145

def get_federal_tax(gpay, code):
    tax = 0
    match code:
        case 0:
            tax = gpay * 0.23
        case 1:
            tax = gpay * 0.21
        case 2:
            tax = gpay * 0.195
        case 3:
            tax = gpay * 0.185
        case _:
            tax = gpay * (0.18 - ((code - 4) * 0.005))
    return tax

print(get_soc_sec_tax(750))
print(get_soc_sec_tax(1550))
print(get_soc_sec_tax(1100))

print(get_medicare_tax(750))
print(get_medicare_tax(1550))
print(get_medicare_tax(1100))

print(get_federal_tax(750, 0))
print(get_federal_tax(1550, 2))
print(get_federal_tax(1100, 5))
