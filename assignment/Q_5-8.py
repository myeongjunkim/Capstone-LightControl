from math import *

g = 9.807 

def get_weight_per_unit_length(d, r):
    w = r*(pi*d**2/4)
    return w

def get_I(d):
    I = (pi*d**4)/64
    return I

def get_max_deflection_of_shaft(w,l,E,I):
    max_d = 5*(w*l**4) / (384*E*I)
    return max_d

def get_critical_speed_of_shaft(d0):
    N0 = (30/pi)*(g*1000/d0)**(1/2)
    return N0
    
def get_max_deflection_of_pully(P, l, E, I):
    max_d = (P*l**3) / (48*E*I)
    return max_d

def get_critical_speed_of_pully(max_d1):
    N1 = (30/pi)*(g*1000/max_d1)**(1/2)
    return N1

def get_critical_speed(N0, N1):
    return 1/((1/N0**2 + 1/N1**2)**(1/2))
    
# main

d = 50; l = 800;    #[mm]
E = 206*10**3;      #[Mpa]
r = 0.0078          #[kgf/cm^3]
P = 600             #[N]

w = get_weight_per_unit_length(d/10, r)
I = get_I(d)
max_d0 = get_max_deflection_of_shaft(w, l, E, I)
max_d1 = get_max_deflection_of_pully(P, l, E, I)

N0 = get_critical_speed_of_shaft(max_d0)
N1 = get_critical_speed_of_pully(max_d1)
Nc = get_critical_speed(N0, N1)

print("\n<위험속도 Nc 구하기>\n")
print("단위길이당 중량 : ", round(w,2), "[N/mm]")
print("단면 2차 모멘트 I :", round(I,2), "[mm^4]")
print("자중에 의한 최대 처짐량 max_d :", round(max_d0,3), "[mm]")
print("풀리에 의한 최대 처짐량 max_d :", round(max_d1,3), "[mm]")
print("자중에 의한 위험속도 N0 :", round(N0,2), "[rpm]")
print("풀리에 의한 위험속도 N1 :", round(N1,2), "[rpm]")
print("위험속도 Nc :", round(Nc,2), "[rpm]")
print("")
