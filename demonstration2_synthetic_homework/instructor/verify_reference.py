"""Reproduce the reference calculations using only Python's standard library."""
import math,json
from pathlib import Path
h=6.62607015e-34;c=299792458.;k=1.380649e-23;sigma=5.670374419e-8
S0=1361.;T=288.15;T0=283.15;TE=242.15;RE=6371000.;z=300000.
def B_lambda(l,T):return 2*h*c*c/l**5/math.expm1(h*c/(l*k*T))
def B_nu(n,T):return 2*h*n**3/c**2/math.expm1(h*n/(k*T))
def B_s(s,T):return 2*h*c*c*s**3/math.expm1(h*c*s/(k*T))
def TB_lambda(l,I):return h*c/(l*k*math.log1p(2*h*c*c/(l**5*I)))
def TB_s(s,I):return h*c*s/(k*math.log1p(2*h*c*c*s**3/I))
Tb=TB_lambda(1e-5,9.8e6)
FE=sigma*TE**4*(RE/(RE+z))**2
results={'brightness_temperature_K':Tb,'radiance_07um_per_um':B_lambda(.7e-6,T)*1e-6,'radiance_1000cm_per_cm_inv':B_s(1e5,T)*100,'radiance_31_4GHz_per_Hz':B_nu(31.4e9,T),'Venus_effective_temperature_K':(S0*.23/(4*.72**2*sigma))**.25,'Earth_IR_W_m2':FE,'satellite_temperature_K':(T0**4+FE/(6*sigma))**.25,'satellite_temperature_increase_K':(T0**4+FE/(6*sigma))**.25-T0,'satellite_no_dilution_K':(T0**4+TE**4/6)**.25}
for a in [.2,.8]:results[f'emissivity_albedo_{a}']=(S0*(1-a)+200)/(6*sigma*T0**4)
# Inverse Planck, Jacobian, and energy balance checks.
assert math.isclose(B_lambda(1e-5,Tb)*1e-6,9.8,rel_tol=1e-12)
for l in [.7e-6,10e-6,.01]:
 assert math.isclose(B_lambda(l,T)*(l*l/c),B_nu(c/l,T),rel_tol=1e-12)
 assert math.isclose(B_lambda(l,T)*l*l,B_s(1/l,T),rel_tol=1e-12)
 assert math.isclose(TB_s(1/l,B_s(1/l,T)),T,rel_tol=1e-12)
for a in [.2,.8]:
 e=results[f'emissivity_albedo_{a}'];tn=results['satellite_temperature_K']
 assert math.isclose(6*e*sigma*tn**4,S0*(1-a)+200+e*FE,rel_tol=1e-12)
# Check the small optical-radiance discrepancy due to rounded constants.
results['07um_per_m_rounded_constants']=2*6.626e-34*(3e8)**2/(7e-7)**5/math.expm1(6.626e-34*3e8/(7e-7*1.38e-23*T))
results['radar_conversions'] = {str(n): {'wavelength_cm': c/n*100, 'wavenumber_m_inv': n/c} for n in [6e9,98e9]}
results['photon_650nm_J'] = h*c/(650e-9)
results['photon_650nm_eV'] = results['photon_650nm_J']/1.602176634e-19
results['window_wavenumbers_cm_inv'] = [1/(l*1e-6)/100 for l in [8,12]]
results['fluxes_in_units_of_F0'] = {'downward':0.5, 'upward':0.3*0.5, 'actinic_direct':1., 'actinic_reflected':2*0.3*0.5, 'actinic_total':1+2*0.3*0.5}
print(json.dumps(results,indent=2))
Path(__file__).with_name('verified_reference_values.json').write_text(json.dumps(results,indent=2))
