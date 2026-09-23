"""Build entirely fictional workshop submissions; never reads student records."""
from pathlib import Path
import json, shutil, zipfile, hashlib
from xml.sax.saxutils import escape
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_LEFT

ROOT = Path(__file__).resolve().parent
PDF = ROOT.parent / 'output/pdf/synthetic_homework'
PDF.mkdir(parents=True, exist_ok=True)
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Answer', fontName='Helvetica', fontSize=10.5, leading=15, spaceAfter=9))
styles.add(ParagraphStyle(name='NoteSmall', fontName='Helvetica', fontSize=9, leading=12, textColor=colors.HexColor('#526174'), spaceAfter=10))

correct = [
[
'Notation: nu is frequency (Hz); s is spectroscopic wavenumber (m^-1), not angular wavenumber; lambda is in metres. B_lambda is per metre of wavelength.',
'Start with B_lambda = (2 h c^2 / lambda^5) / [exp(h c / (lambda k T)) - 1]. Spectral energy is conserved: B_nu |dnu| = B_lambda |dlambda|. Since lambda = c/nu, |dlambda/dnu| = c/nu^2 = lambda^2/c. Thus B_nu = B_lambda lambda^2/c = (2 h nu^3 / c^2) / [exp(h nu / (k T)) - 1]. The absolute Jacobian gives positive radiance.',
'For s = 1/lambda, |dlambda/ds| = 1/s^2 = lambda^2. Hence B_s = B_lambda lambda^2 = (2 h c^2 s^3) / [exp(h c s / (k T)) - 1].',
'For an observed I_lambda, rearrange the wavelength law: exp(h c/(lambda k T)) = 1 + 2 h c^2/(lambda^5 I_lambda). Take the natural logarithm and solve: T_b = h c / {lambda k ln[1 + 2 h c^2/(lambda^5 I_lambda)]}.',
'Likewise, exp(h c s/(k T)) = 1 + 2 h c^2 s^3/I_s, so T_b = h c s / {k ln[1 + 2 h c^2 s^3/I_s]}. I_s must be per m^-1 when s is in m^-1. These are inverse functions for T, not reciprocals of radiance.'
],
[
'At 10 micrometres, lambda = 1.0e-5 m and I_lambda = 9.8 W m^-2 sr^-1 micrometre^-1 = 9.8e6 W m^-2 sr^-1 m^-1. Substituting in the inverse Planck law gives T_b = 299.22 K (26.07 deg C). With no atmospheric attenuation and the blackbody interpretation, this is the inferred surface temperature.',
'For the land surface, T = 15 + 273.15 = 288.15 K. At 0.7 micrometres, B_lambda = 7.4454e-17 W m^-2 sr^-1 m^-1 = 7.4454e-23 W m^-2 sr^-1 micrometre^-1. I used the wavelength Planck law and multiplied its per-metre result by 1e-6.',
'At 1000 cm^-1, s = 1.0e5 m^-1. B_s = 8.1355e-4 W m^-2 sr^-1 (m^-1)^-1. A 1 cm^-1 interval is 100 m^-1, giving 0.081355 W m^-2 sr^-1 (cm^-1)^-1.',
'At nu = 31.4e9 Hz, B_nu = 8.7059e-17 W m^-2 sr^-1 Hz^-1 using the frequency Planck law. The small h nu/(k T) also makes the Rayleigh-Jeans approximation a useful check.'
],
[
'Use lambda = c/nu and s = nu/c, with c = 299792458 m/s. For 6 GHz: lambda = 0.0499654 m = 4.99654 cm; s = 20.0138 m^-1. For 98 GHz: lambda = 0.00305911 m = 0.305911 cm; s = 326.893 m^-1.',
'For red light, E = h c/lambda = (6.62607015e-34)(299792458)/(650e-9) = 3.05607e-19 J. Divide by 1.602176634e-19 J/eV to obtain 1.90745 eV.',
'The window endpoints are 8 micrometres = 8e-4 cm and 12 micrometres = 1.2e-3 cm. Their reciprocals are 1250 and 833.33 cm^-1. Thus the window is 833.33-1250 cm^-1; wavenumber decreases as wavelength increases.'
],
[
'Use S_0 = 1361 W m^-2 at 1 AU and sigma = 5.670374419e-8 W m^-2 K^-4. At Venus S_V = S_0/(0.72)^2. Absorbed power is (1 - 0.77) S_V pi R^2; outgoing power is 4 pi R^2 sigma T_E^4.',
'Equating the powers gives T_E = [(1 - 0.77) S_0/(4 sigma (0.72)^2)]^(1/4) = 227.15 K.',
'T_E describes the emission to space, not the surface. Venus has a very optically thick infrared atmosphere; radiation escapes mainly from higher, colder layers. The greenhouse effect and the atmospheric temperature profile allow a surface near 750 K while the planet emits to space at a much lower effective temperature.'
],
[
'For F_0 = 1, mu_0 = 0.5 and albedo rho = 0.3, integrating the collimated beam with the projection factor gives F_down = mu_0 F_0 = 0.5. The reflected upward flux is F_up = rho F_down = 0.15. Values here use the irradiance units of F_0.',
'The reflected Lambertian radiance is L_r = F_up/pi. The direct actinic contribution has no cosine weighting, so A_direct = integral I_direct dOmega = F_0 = 1.',
'The upward hemisphere contributes A_reflected = integral L_r dOmega = 2 pi L_r = 2 F_up = 0.30. Therefore the total actinic flux at the surface is A = 1 + 0.30 = 1.30.'
],
[
'Each cube face has area 1 m^2. At T_0 = 283.15 K, solar absorption plus instrument heat balances emission from all six faces: (1 - alpha) S_0 (1 m^2) + 200 W = 6 epsilon sigma (1 m^2) T_0^4. Assume uniform temperature and thermal emissivity.',
'Thus epsilon = [(1 - alpha) S_0 + 200]/(6 sigma T_0^4). For alpha = 0.2, absorbed plus internal power is 1288.8 W and epsilon = 0.58933. For alpha = 0.8, it is 472.2 W and epsilon = 0.21592.',
'Take T_Earth = 242.15 K and R_Earth = 6371 km. Assume the designated face points toward the Earth centre, with a uniform blackbody Earth disk, no eclipse, and unchanged solar input. Irradiance on that face is F_E = sigma T_Earth^4 [R_Earth/(R_Earth + 300 km)]^2 = 177.82 W m^-2.',
'For a grey thermal surface, Kirchhoff\'s law gives thermal absorptivity = epsilon; the solar absorptivity (1 - alpha) is a different quantity. The added absorbed Earth power is epsilon F_E (1 m^2).',
'The revised balance is (1 - alpha) S_0 + 200 + epsilon F_E = 6 epsilon sigma T_new^4. Subtract the original balance to obtain T_new^4 = T_0^4 + F_E/(6 sigma).',
'Both housings therefore reach T_new = 288.74 K (15.59 deg C), an increase of 5.59 K. Epsilon cancels under the stated grey-body assumptions; it does not mean Earth absorption is independent of emissivity.'
]
]

samples = []
def add(name, answers, scores, notes):
    samples.append(dict(name=name, answers=answers, scores=scores, notes=notes))

add('Tony Stark', correct, [[5,5,5,5],[8,4,4,4],[6,4,5],[4,3,3],[6,3,3,3],[4,6,3,3,2,2]],
    ['All four transformations/inverses are derived with consistent spectral conventions.',
     'All results and spectral-density conversions are correct.', 'All conversions and units are correct.',
     'Correct energy balance, temperature, and greenhouse explanation.', 'Correct projected and actinic fluxes.',
     'Complete solution with explicit geometry and thermal absorptivity assumptions.'])

add('Peter Parker', [
    correct[0][:4] + ['I did not finish the wavenumber brightness-temperature inverse.'],
    [correct[1][0], 'I used T = 288.15 K. At 0.7 micrometres I obtain 7.4454e-17 W m^-2 sr^-1 micrometre^-1 from the wavelength formula; I kept its numerical value when changing the spectral unit label.',correct[1][2],correct[1][3]],
    correct[2], correct[3][:2] + ['I think the difference is simply because the surface is closer to the Sun than the top of the atmosphere; I would not need infrared absorption to explain it.'],
    correct[4][:2] + ['The reflected actinic component is 2 pi L_r = 0.30. Adding the two contributions, I report total actinic flux = 1.15.'],
    correct[5][:2] + ['I have not completed the calculation including Earth thermal emission.']
], [[5,5,5,0],[8,0,4,4],[6,4,5],[4,3,0],[6,3,3,0],[4,6,0,0,0,0]],
    ['Wavenumber inverse omitted: -5.', 'Optical result is mislabeled per micrometre, a factor of 1e6 error: -4.',
     'All conversions correct.', 'Surface-to-orbit distance does not explain the greenhouse temperature difference: -3.',
     'Components are correct, but their final sum is wrong: -3. Do not also penalize the reflected component.',
     'Both emissivities correct; entire Earth-heating extension omitted: -10.'])

add('Natasha Romanoff', [
    correct[0][:3] + ['For the inverse I would write T_b = 1/B_lambda, or 1/B_s for wavenumber. I have not isolated temperature algebraically.'],
    [correct[1][0], 'For the three radiances at 15 deg C I have not completed numerical calculations or a conversion to kelvin.'],
    correct[2][:2] + ['For the 8-12 micrometre window, I take reciprocals of 8 and 12 and obtain 0.125 to 0.0833 cm^-1.'],
    correct[3][:2] + ['My explanation of 750 K is that the cloud layer is a source of additional solar energy. I have not considered the altitude of infrared emission to space.'],
    correct[4][:2] + ['I treat reflected actinic flux as equal to upward irradiance, 0.15, because both describe reflected light. My total actinic flux is therefore 1.15.'],
    [correct[5][0], 'Using S_0 = 1361 W m^-2 gives absorbed solar plus instrument powers 1288.8 W and 472.2 W. My numerical substitution is epsilon = P/(sigma T_0^4), giving 3.536 and 1.296, respectively. These exceed one, but I have not located the error.', 'I have not attempted the Earth thermal-radiation extension.']
], [[5,5,0,0],[8,0,0,0],[6,4,0],[4,3,0],[6,3,0,0],[4,2,0,0,0,0]],
    ['Spectral conversions correct; both inverse functions replaced by reciprocals: -10.',
     'Correct brightness temperature; all three emitted-radiance calculations omitted: -12.',
     'Radar and photon conversions correct; window reciprocals use inconsistent units: -5.',
     'Balance and temperature correct; clouds do not create energy and greenhouse mechanism is missing: -3.',
     'Reflected actinic flux lacks the factor 2: -3; final total consequently wrong: -3 under the separate final-result criterion. Preserve all direct/irradiance credit.',
     'Correct six-face balance: 4/4. Emissivities: 2/6 for both correct absorbed powers, but neither numerical emissivity is correct; six-face factor lost in substitution. Earth extension: 0/10.'])

add('Thor Odinson', [
    correct[0][:2] + ['For wavenumber I just set s = 1/lambda in B_lambda and keep the same spectral density, giving B_s = 2 h c^2 s^5/[exp(h c s/(k T)) - 1]. For brightness temperature I propose 1/B_lambda and 1/B_s.'],
    [correct[1][0], 'I did not complete the three emitted-radiance calculations for the 15 deg C surface.'],
    [correct[2][0], 'For the photon, E = h nu, and I substitute 650 as nu, giving 4.307e-31 eV.', 'I assume an 8-12 micrometre window means a wavenumber window of 8-12 cm^-1.'],
    [correct[3][0], 'I have not evaluated the fourth root. I think the high surface temperature comes from heat generated by the clouds.'],
    ['I take downward flux to be F_0 = 1 and upward flux to be rho F_0 = 0.30, without a solar-zenith projection.', 'The direct actinic flux is integral I_direct dOmega = F_0 = 1; there is no cosine weighting for this quantity. I have not calculated the reflected actinic contribution or total.'],
    [correct[5][0], 'I have not solved this balance for either emissivity or included Earth emission.']
], [[5,0,0,0],[8,0,0,0],[6,0,0],[4,0,0],[0,3,0,0],[4,0,0,0,0,0]],
    ['Frequency conversion correct; wavenumber Jacobian missing and both inverses incorrect: -15.',
     'Brightness temperature correct; three radiances omitted: -12.',
     'Radar conversions correct; photon calculation confuses wavelength/frequency and energy units, and window conversion is wrong: -9.',
     'Correct global energy balance earns 4; temperature unevaluated and explanation incorrect: -6.',
     'Correct direct actinic flux earns 3; projected fluxes wrong and reflected/total actinic answers omitted: -12.',
     'Correct initial six-face balance earns 4; remaining work omitted: -16.'])

titles = ['Planck functions and brightness temperature','Surface radiance','Spectral conversions','Venus energy balance','Lambertian reflection and actinic flux','Satellite thermal balance']
constants = 'Constants used: h = 6.62607015e-34 J s; c = 299792458 m/s; k = 1.380649e-23 J/K; sigma = 5.670374419e-8 W m^-2 K^-4; S_0 = 1361 W m^-2. Natural logarithms; SI units unless stated otherwise.'
def para(text, style='Answer'):
    return Paragraph(escape(text), styles[style])

def footer(c, d):
    c.setStrokeColor(colors.HexColor('#cbd5e1'));c.line(45,43,567,43)
    c.setFont('Helvetica',8);c.setFillColor(colors.HexColor('#526174'))
    c.drawString(45,29,'FICTIONAL WORKSHOP SAMPLE | No real student work or identity')
    c.drawRightString(567,29,str(d.page))

def render(path, story):
    SimpleDocTemplate(str(path),pagesize=(612,792),leftMargin=45,rightMargin=45,topMargin=40,bottomMargin=55,
        title=path.stem.replace('_',' '),author='AI cowork workshop - synthetic materials').build(story,onFirstPage=footer,onLaterPages=footer)

rubric=json.loads((ROOT/'instructor/rubric.json').read_text())
targets=[100,75,50,30]
key=['# Instructor key: fictional PHYS623 Homework 1 submissions','',
     'These are designed scores under the workshop rubric, not real grades or a guarantee that an independent grader will choose identical partial credit. All answers were newly composed from the assignment and checked reference calculations; no real student answers were used. Character names are fictional labels, not evidence for grading.', '',
     'Keep this key outside the grading input folder. Grade the four PDFs first, then reveal this key. To demonstrate anonymous reporting, ask for Submission A-D in the report and keep the Marvel names only in a separate identity mapping.', '',
     '## Rubric and conventions','',
     'Problem totals: P1 20, P2 20, P3 15, P4 10, P5 15, P6 20 (100 overall). The criterion-level rubric is in rubric.json. Accept equivalent correctly labeled spectral units and reasonable rounding. P6 assumes a nadir-facing face, a uniformly emitting Earth disk and grey thermal absorptivity equal to emissivity. Other justified geometry conventions require instructor judgment.', '',
     'For the P6 emissivity criterion (6 points): award 1 point for each correct absorbed-plus-internal power and 2 points for each correct emissivity, with valid supporting work. For P5, component derivations and the final total are separate criteria; retain correct component credit when the final result is wrong. All other criteria here are fully met or clearly omitted/incorrect.', '']

for sample,target in zip(samples,targets):
    name=sample['name']; stem=name.replace(' ','_')+'_HW1'
    total=sum(map(sum,sample['scores']));assert total==target
    story=[];md=[f'# {name} - Homework 1','', 'FICTIONAL WORKSHOP SAMPLE. No real student work or identity.','', 'PHYS623 Atmospheric Radiation | Fall 2025 assignment used as a practice exercise.','',constants,'']
    for i,answers in enumerate(sample['answers']):
        if i%2==0:
            if i: story.append(PageBreak())
            story += [para(name+' | Homework 1','Title'),para('PHYS623 Atmospheric Radiation - fictional practice submission','NoteSmall')]
            if i==0:story.append(para(constants,'NoteSmall'))
        story.append(para(f'Problem {i+1}: {titles[i]}','Heading2'))
        md += [f'## Problem {i+1}: {titles[i]}','']
        for a in answers:story.append(para(a));md += [a,'']
        story.append(Spacer(1,8))
    render(PDF/(stem+'.pdf'),story)
    shutil.copy2(PDF/(stem+'.pdf'),ROOT/'submissions'/(stem+'.pdf'))
    (ROOT/'submissions'/(stem+'.md')).write_text('\n'.join(md))
    key += [f'## {name}: {total}/100','', '| Problem | Score | Criterion scores (rubric order) | Rationale |','| --- | --- | --- | --- |']
    for i,(scores,note) in enumerate(zip(sample['scores'],sample['notes'])):
        maxima=list(rubric[f'P{i+1}']['criteria'].values())
        assert len(scores)==len(maxima) and all(0<=s<=m for s,m in zip(scores,maxima))
        key.append(f'| P{i+1} (submission page {i//2+1}) | {sum(scores)}/{sum(maxima)} | '+', '.join(f'{s}/{m}' for s,m in zip(scores,maxima))+f' | {note} |')
    key += ['']

(ROOT/'instructor/Instructor_key.md').write_text('\n'.join(key))
(ROOT/'instructor/expected_scores.json').write_text(json.dumps([{k:v for k,v in s.items() if k!='answers'} | {'total':t} for s,t in zip(samples,targets)],indent=2))
key_story=[para('Instructor key','Title'),para('Fictional submissions - reveal only after independent grading','NoteSmall')]
key_story += [para(p) for p in [key[2],key[4],key[8],key[10]]]
for s,t in zip(samples,targets):
    key_story += [PageBreak(),para(f"{s['name']}: {t}/100",'Title')]
    for i,(scores,note) in enumerate(zip(s['scores'],s['notes'])):
        criteria=list(rubric[f'P{i+1}']['criteria'].items())
        key_story += [para(f'P{i+1}: {sum(scores)}/{rubric[f"P{i+1}"]["total"]} - submission page {i//2+1}','Heading2'),para('; '.join(f'{label}: {score}/{maximum}' for (label,maximum),score in zip(criteria,scores)),'NoteSmall'),para(note)]
render(PDF/'Instructor_key.pdf',key_story)
shutil.copy2(PDF/'Instructor_key.pdf',ROOT/'instructor/Instructor_key.pdf')

with zipfile.ZipFile(ROOT/'Four_fictional_submissions.zip','w',zipfile.ZIP_DEFLATED) as z:
    for p in sorted((ROOT/'submissions').glob('*.pdf')):z.write(p,p.name)
assert len(zipfile.ZipFile(ROOT/'Four_fictional_submissions.zip').namelist())==4
manifest={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((ROOT/'submissions').glob('*.pdf'))}
(ROOT/'instructor/submission_hashes.json').write_text(json.dumps(manifest,indent=2))
print('Built four fictional submissions and a separate instructor key. Scores:',targets)
