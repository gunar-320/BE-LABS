import math
f=float(input("Enter Frequency "))
L=float(input("Enter Inductance "))
C=float(input("Enter Capacitance "))
R=float(input("Enter Resistance "))
w=2*3.14*f
print("Angular frequency is ",w)
phi = (w*L-(1/(w*C)))/R
z= math.degrees(math.atan(phi))
print("Phase difference between Input Voltage and Input Current is ",z)
Vmax=float(input("Enter Voltage "))
V=Vmax/1.414
Za=w*L-1/(w*C)
Z=(Za**2)+R**2
Irms = V/math.sqrt(Z)
VL = Irms*w*L
VC = Irms/(w*C)
VR = Irms*R
print("Vrms is ",V)
print("Irms is ",Irms)
print("VL is ",VL)
print("VC is ",VC)
print("VR IS ",VR)




