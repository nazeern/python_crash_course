#calculating eccentricity of ellipse

#gathering inputs from user
x=int(raw_input("input x : "))
y=int(raw_input("input y : "))
a=int(raw_input("input a : "))
b=int(raw_input("input b : "))

#assigning corresponding variables
c=x**2
d=y**2
f=a**2
g=b**2

#Using the eccentricity formula
none=c/f
ntwo=d/g
eccentricity=none+ntwo
print "the eccentricity of the ellipse is %s " %eccentricity
