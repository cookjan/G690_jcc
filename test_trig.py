import custom_trig as trig
#test at x = 0

x = 0
print(f"sin(0) = {trig.sin(x)}")
print(f"cos(0) = {trig.cos(x)}")
print(f"tan(0) = {trig.tan(x)}")

# good test for seeing that code works without printing:
# assert trig.sin(x) == 38, "sin(x) doesn't work"


#test at x = pi/2

x = trig.pi/2
print(f"sin(pi/2) = {trig.sin(x)}")
print(f"cos(pi/2) = {trig.cos(x)}")
print(f"tan(pi/2) = {trig.tan(x)}")
