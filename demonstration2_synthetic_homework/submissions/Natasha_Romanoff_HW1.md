# Natasha Romanoff - Homework 1

FICTIONAL WORKSHOP SAMPLE. No real student work or identity.

PHYS623 Atmospheric Radiation | Fall 2025 assignment used as a practice exercise.

Constants used: h = 6.62607015e-34 J s; c = 299792458 m/s; k = 1.380649e-23 J/K; sigma = 5.670374419e-8 W m^-2 K^-4; S_0 = 1361 W m^-2. Natural logarithms; SI units unless stated otherwise.

## Problem 1: Planck functions and brightness temperature

Notation: nu is frequency (Hz); s is spectroscopic wavenumber (m^-1), not angular wavenumber; lambda is in metres. B_lambda is per metre of wavelength.

Start with B_lambda = (2 h c^2 / lambda^5) / [exp(h c / (lambda k T)) - 1]. Spectral energy is conserved: B_nu |dnu| = B_lambda |dlambda|. Since lambda = c/nu, |dlambda/dnu| = c/nu^2 = lambda^2/c. Thus B_nu = B_lambda lambda^2/c = (2 h nu^3 / c^2) / [exp(h nu / (k T)) - 1]. The absolute Jacobian gives positive radiance.

For s = 1/lambda, |dlambda/ds| = 1/s^2 = lambda^2. Hence B_s = B_lambda lambda^2 = (2 h c^2 s^3) / [exp(h c s / (k T)) - 1].

For the inverse I would write T_b = 1/B_lambda, or 1/B_s for wavenumber. I have not isolated temperature algebraically.

## Problem 2: Surface radiance

At 10 micrometres, lambda = 1.0e-5 m and I_lambda = 9.8 W m^-2 sr^-1 micrometre^-1 = 9.8e6 W m^-2 sr^-1 m^-1. Substituting in the inverse Planck law gives T_b = 299.22 K (26.07 deg C). With no atmospheric attenuation and the blackbody interpretation, this is the inferred surface temperature.

For the three radiances at 15 deg C I have not completed numerical calculations or a conversion to kelvin.

## Problem 3: Spectral conversions

Use lambda = c/nu and s = nu/c, with c = 299792458 m/s. For 6 GHz: lambda = 0.0499654 m = 4.99654 cm; s = 20.0138 m^-1. For 98 GHz: lambda = 0.00305911 m = 0.305911 cm; s = 326.893 m^-1.

For red light, E = h c/lambda = (6.62607015e-34)(299792458)/(650e-9) = 3.05607e-19 J. Divide by 1.602176634e-19 J/eV to obtain 1.90745 eV.

For the 8-12 micrometre window, I take reciprocals of 8 and 12 and obtain 0.125 to 0.0833 cm^-1.

## Problem 4: Venus energy balance

Use S_0 = 1361 W m^-2 at 1 AU and sigma = 5.670374419e-8 W m^-2 K^-4. At Venus S_V = S_0/(0.72)^2. Absorbed power is (1 - 0.77) S_V pi R^2; outgoing power is 4 pi R^2 sigma T_E^4.

Equating the powers gives T_E = [(1 - 0.77) S_0/(4 sigma (0.72)^2)]^(1/4) = 227.15 K.

My explanation of 750 K is that the cloud layer is a source of additional solar energy. I have not considered the altitude of infrared emission to space.

## Problem 5: Lambertian reflection and actinic flux

For F_0 = 1, mu_0 = 0.5 and albedo rho = 0.3, integrating the collimated beam with the projection factor gives F_down = mu_0 F_0 = 0.5. The reflected upward flux is F_up = rho F_down = 0.15. Values here use the irradiance units of F_0.

The reflected Lambertian radiance is L_r = F_up/pi. The direct actinic contribution has no cosine weighting, so A_direct = integral I_direct dOmega = F_0 = 1.

I treat reflected actinic flux as equal to upward irradiance, 0.15, because both describe reflected light. My total actinic flux is therefore 1.15.

## Problem 6: Satellite thermal balance

Each cube face has area 1 m^2. At T_0 = 283.15 K, solar absorption plus instrument heat balances emission from all six faces: (1 - alpha) S_0 (1 m^2) + 200 W = 6 epsilon sigma (1 m^2) T_0^4. Assume uniform temperature and thermal emissivity.

Using S_0 = 1361 W m^-2 gives absorbed solar plus instrument powers 1288.8 W and 472.2 W. My numerical substitution is epsilon = P/(sigma T_0^4), giving 3.536 and 1.296, respectively. These exceed one, but I have not located the error.

I have not attempted the Earth thermal-radiation extension.
