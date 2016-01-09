import numpy as np
from scipy.optimize import curve_fit
import scipy.constants
import data
from uncertainties import ufloat

# erste Zeitmessung


def f(x,  m, b):
    return m * x + b


params, covar = curve_fit(f,
                          data.dyn.radius,
                          data.dyn.time,
                          )
error = np.sqrt(np.diag(covar))

m = ufloat(params[0], error[0]) * 10 ** 6
b = ufloat(params[1], error[1])
l = ufloat(0.02998, 0.00025)
r = ufloat(0.01763, 0.00028)
m_zyl = ufloat(0.22260, 0.00118)
print('linear fit:', m, b)

D_dyn = 8 * np.pi ** 2 * m_zyl / m
I_D = (D_dyn * b / (4 * np.pi ** 2)) - 2 * ((l ** 2 / 12) + (r ** 2 / 4))

print('dynamic:', D_dyn, I_D)
D_stat = ufloat(3.08, 0.61) * 10 ** -2

T_kug = ufloat(1.656, 0.045)
T_zyl = ufloat(1.687, 0.012)


I_kugdyn = T_kug ** 2 / (4 * (np.pi ** 2)) * D_dyn + I_D
I_zyldyn = T_zyl ** 2 / (4 * (np.pi ** 2)) * D_dyn + I_D

I_kugstat = T_kug ** 2 / (4 * (np.pi ** 2)) * D_stat + I_D
I_zylstat = T_zyl ** 2 / (4 * (np.pi ** 2)) * D_stat + I_D


print('Traegheit_dyn:', I_kugdyn, I_zyldyn)
print('Traegheit_stat:', I_kugstat, I_zylstat)

R_kug = ufloat(13.743, 0.034) * 10 ** -2
M_kug = 0.8125
R_zyl = ufloat(8.118, 0.074) * 10 ** -2
M_zyl = 1.9738
L_zyl = ufloat(14.183, 0.076) * 10 ** -2

I_kug = 2 / 5 * M_kug * R_kug ** 2
I_zyl = 1 / 2 * M_zyl * R_zyl ** 2


print('Traegheit_theo:', I_kug, I_zyl)

T_pos1 = ufloat(0.557, 0.027)
T_pos2 = ufloat(0.812, 0.004)

I_pos1dyn = T_pos1 ** 2 * D_dyn / (4 * np.pi ** 2)
I_pos1stat = T_pos1 ** 2 * D_stat / (4 * np.pi ** 2)
I_pos2dyn = T_pos2 ** 2 * D_dyn / (4 * np.pi ** 2)
I_pos2stat = T_pos2 ** 2 * D_stat / (4 * np.pi ** 2)

print('Taegheit_pos1', I_pos1dyn, I_pos1stat)
print('Taegheit_pos2', I_pos2dyn, I_pos2stat)

R_bein = ufloat(17.77, 5.346) * 10 ** -3 / 2
L_bein = ufloat(150.81, 3.52) * 10 ** -3
R_arm = ufloat(13.54, 2.946) * 10 ** -3 / 2
L_arm = ufloat(140.05, 1.34) * 10 ** -3
R_kopf = ufloat(24.01, 7.77) * 10 ** -3 / 2
L_kopf = ufloat(54.48, 0) * 10 ** -3
R_torso = ufloat(35.49, 6.39) * 10 ** -3 / 2
L_torso = ufloat(54.48, 0) * 10 ** -3


def Vol_z(R, L):
    return np.pi * R ** 2 * L

V_figur = 2 * Vol_z(R_bein, L_bein) + 2 * Vol_z(R_arm, L_arm) + Vol_z(R_kopf, L_kopf) + Vol_z(R_torso, L_torso)


print('V_figur', V_figur)


V_bein = Vol_z(R_bein, L_bein)
V_arm = Vol_z(R_arm, L_arm)
V_kopf = Vol_z(R_kopf, L_kopf)
V_torso = Vol_z(R_torso, L_torso)


print('V_bein', V_bein)
print('V_arm', V_arm)
print('V_kopf', V_kopf)
print('V_torso', V_torso)

M = 0.16253

M_bein = M * (V_bein / V_figur)
M_arm = M * (V_arm / V_figur)
M_kopf = M * (V_kopf / V_figur)
M_torso = M * (V_torso / V_figur)

print('M_bein', M_bein)
print('M_arm', M_arm)
print('M_kopf', M_kopf)
print('M_torso', M_torso)

I_bein = 1 / 2 * M_bein * R_bein ** 2
I_arm = 1 / 2 * M_arm * R_arm ** 2
I_kopf = 1 / 2 * M_kopf * R_kopf ** 2
I_torso = 1 / 2 * M_torso * R_torso ** 2

print('I_bein', I_bein)
print('I_arm', I_arm)
print('I_kopf', I_kopf)
print('I_torso', I_torso)

I_ges1 = I_torso + I_kopf + 2 * (R_torso ** 2 * (M_arm + M_bein) + I_arm + I_bein)
print('R_torso', R_torso)
print('I_ges1', I_ges1)

I_arm2 = M_arm * (R_arm ** 2 / 4 + L_arm ** 2 / 12)

I_ges2 = I_torso + I_kopf + 2 * ((R_torso + 1 / 2 * L_arm) ** 2 * M_arm + R_torso ** 2 * M_bein + I_arm2 + I_bein)

print('I_ges2', I_ges2)
