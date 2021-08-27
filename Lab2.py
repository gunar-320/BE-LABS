import math
f=float(input("Enter Frequency "))
L=0.001
C=0.0001
R=10
Rint = 12.5
w=2*3.14*f
print("Angular frequency is ",w)
phi = (w*L-(1/(w*C)))/(R+Rint) #Refer formula in handbook!
z= math.degrees(math.atan(phi))
print("Phase difference between Input Voltage and Input Current is ",z)
Vmax=5
V=Vmax/1.414
Za=w*L-1/(w*C)
Z=(Za**2)+(R+Rint)**2
Irms = V/math.sqrt(Z)
ZL = (w*L)**2+Rint**2
VL = Irms*math.sqrt(ZL)
VC = Irms/(w*C) #Will remain constant
VR = Irms*R #Will remain constant
print("Vrms is ",V)
print("Irms is ",Irms)
print("VL is ",VL)
print("VC is ",VC)
print("VR IS ",VR)
print("Phase difference between Inductor and Current is ",math.degrees(math.atan(w*L/12.5)))





