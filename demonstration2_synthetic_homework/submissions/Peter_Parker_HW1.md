# Peter Parker - Homework 1

FICTIONAL WORKSHOP SAMPLE. No real student work or identity.

PHYS623 Atmospheric Radiation | Fall 2025 assignment used as a practice exercise.

Constants used: h = 6.62607015e-34 J s; c = 299792458 m/s; k = 1.380649e-23 J/K; sigma = 5.670374419e-8 W m^-2 K^-4; S_0 = 1361 W m^-2. Natural logarithms; SI units unless stated otherwise.

## Problem 1: Planck functions and brightness temperature

Notation: nu is frequency (Hz); s is spectroscopic wavenumber (m^-1), not angular wavenumber; lambda is in metres. B_lambda is per metre of wavelength.

Start with B_lambda = (2 h c^2 / lambda^5) / [exp(h c / (lambda k T)) - 1]. Spectral energy is conserved: B_nu |dnu| = B_lambda |dlambda|. Since lambda = c/nu, |dlambda/dnu| = c/nu^2 = lambda^2/c. Thus B_nu = B_lambda lambda^2/c = (2 h nu^3 / c^2) / [exp(h nu / (k T)) - 1]. The absolute Jacobian gives positive radiance.

For s = 1/lambda, |dlambda/ds| = 1/s^2 = lambda^2. Hence B_s = B_lambda lambda^2 = (2 h c^2 s^3) / [exp(h c s / (k T)) - 1].

For an observed I_lambda, rearrange the wavelength law: exp(h c/(lambda k T)) = 1 + 2 h c^2/(lambda^5 I_lambda). Take the natural logarithm and solve: T_b = h c / {lambda k ln[1 + 2 h c^2/(lambda^5 I_lambda)]}.

I did not finish the wavenumber brightness-temperature inverse.

## Problem 2: Surface radiance

At 10 micrometres, lambda = 1.0e-5 m and I_lambda = 9.8 W m^-2 sr^-1 micrometre^-1 = 9.8e6 W m^-2 sr^-1 m^-1. Substituting in the inverse Planck law gives T_b = 299.22 K (26.07 deg C). With no atmospheric attenuation and the blackbody interpretation, this is the inferred surface temperature.

I used T = 288.15 K. At 0.7 micrometres I obtain 7.4454e-17 W m^-2 sr^-1 micrometre^-1 from the wavelength formula; I kept its numerical value when changing the spectral unit label.

At 1000 cm^-1, s = 1.0e5 m^-1. B_s = 8.1355e-4 W m^-2 sr^-1 (m^-1)^-1. A 1 cm^-1 interval is 100 m^-1, giving 0.081355 W m^-2 sr^-1 (cm^-1)^-1.

At nu = 31.4e9 Hz, B_nu = 8.7059e-17 W m^-2 sr^-1 Hz^-1 using the frequency Planck law. The small h nu/(k T) also makes the Rayleigh-Jeans approximation a useful check.

## Problem 3: Spectral conversions

Use lambda = c/nu and s = nu/c, with c = 299792458 m/s. For 6 GHz: lambda = 0.0499654 m = 4.99654 cm; s = 20.0138 m^-1. For 98 GHz: lambda = 0.00305911 m = 0.305911 cm; s = 326.893 m^-1.

For red light, E = h c/lambda = (6.62607015e-34)(299792458)/(650e-9) = 3.05607e-19 J. Divide by 1.602176634e-19 J/eV to obtain 1.90745 eV.

The window endpoints are 8 micrometres = 8e-4 cm and 12 micrometres = 1.2e-3 cm. Their reciprocals are 1250 and 833.33 cm^-1. Thus the window is 833.33-1250 cm^-1; wavenumber decreases as wavelength increases.

## Problem 4: Venus energy balance

Use S_0 = 1361 W m^-2 at 1 AU and sigma = 5.670374419e-8 W m^-2 K^-4. At Venus S_V = S_0/(0.72)^2. Absorbed power is (1 - 0.77) S_V pi R^2; outgoing power is 4 pi R^2 sigma T_E^4.

Equating the powers gives T_E = [(1 - 0.77) S_0/(4 sigma (0.72)^2)]^(1/4) = 227.15 K.

I think the difference is simply because the surface is closer to the Sun than the top of the atmosphere; I would not need infrared absorption to explain it.

## Problem 5: Lambertian reflection and actinic flux

For F_0 = 1, mu_0 = 0.5 and albedo rho = 0.3, integrating the collimated beam with the projection factor gives F_down = mu_0 F_0 = 0.5. The reflected upward flux is F_up = rho F_down = 0.15. Values here use the irradiance units of F_0.

The reflected Lambertian radiance is L_r = F_up/pi. The direct actinic contribution has no cosine weighting, so A_direct = integral I_direct dOmega = F_0 = 1.

The reflected actinic component is 2 pi L_r = 0.30. Adding the two contributions, I report total actinic flux = 1.15.

## Problem 6: Satellite thermal balance

Each cube face has area 1 m^2. At T_0 = 283.15 K, solar absorption plus instrument heat balances emission from all six faces: (1 - alpha) S_0 (1 m^2) + 200 W = 6 epsilon sigma (1 m^2) T_0^4. Assume uniform temperature and thermal emissivity.

Thus epsilon = [(1 - alpha) S_0 + 200]/(6 sigma T_0^4). For alpha = 0.2, absorbed plus internal power is 1288.8 W and epsilon = 0.58933. For alpha = 0.8, it is 472.2 W and epsilon = 0.21592.

I have not completed the calculation including Earth thermal emission.
