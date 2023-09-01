"""creating cos(z)"""
#using formula cos(z)=1/2(e**(i*z)+(e**(-i*z)))
#define e from exercise 1c
e = 2.7182818284590455

#define pi from exercise 1b

pi = 3.1416926635905345

#define i
i = 1.0j

#define cos as a function with angle z in radians
def cos(z):
  cos_z = 1/2*((e**(i*z))+(e**(-i*z)))
  return cos_z

#convert degrees into radians
def deg2rad(deg):
  rad = deg*pi/180
  return rad


"""creating exp(w)"""
#using formula exp(w) = e**(w*i)

#define exp as a function with w
def exp(w):
  exp_w = e**(w)
  return exp_w


"""creating sin(y)"""
#using formula sin(y) = 1/2(e**(i*z)+(e**(-i*z)))

#define sin as a function with y
def sin(y):
  sin_y = 1/2*(e**(i*y)-(e**(-i*y)))
  return sin_y


"""creating tan(x)"""
#using formula tan(x) = sin(x)/cos(x)

# functions sin and cos are defined in previous cells, as well as degrees to radians

#define tan as a function with x
def tan(x):
  tan_x = (sin(x))/(cos(x))
  return tan_x