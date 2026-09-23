"""Generate a short, entirely fictional grading exercise. No outside inputs."""
from pathlib import Path
from xml.sax.saxutils import escape
import json, shutil, zipfile
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

ROOT=Path(__file__).resolve().parent
OUT=ROOT.parent/'output/pdf/avengers101'
OUT.mkdir(parents=True,exist_ok=True)
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='BodyCopy',fontName='Helvetica',fontSize=10.5,leading=14,spaceAfter=9))
styles.add(ParagraphStyle(name='SmallCopy',fontName='Helvetica',fontSize=9,leading=12,spaceAfter=8,textColor=colors.HexColor('#455467')))
questions=[
 ('Is that actually Doom?', 'How would you check whether the villain is Dr. Doom or a Doombot?', ['independent identity check','specific decoy clue','acknowledgment of uncertainty','reversible next step']),
 ('Assemble a team', 'Choose three heroes and explain how they would work together.', ['three named heroes','distinct roles','coordination method','backup plan']),
 ('Protect the public', 'Explain how you would get civilians out of the fictional danger zone.', ['evacuation route','safe meeting place','accessibility assistance','headcount or missing-person check']),
 ('The dramatic shield', 'Invent a harmless, clearly imaginary way to switch off Doom\'s Plot Armor Shield.', ['imaginary mechanism explained','limitation','safe test','fallback if it fails']),
 ('The after-action meeting', 'Write a tiny debrief after the mission.', ['outcome','evidence supporting that outcome','one mistake owned by the team','specific improvement'])
]
samples=[
 ('Shuri',[
 'I compare his armor signature with an independent Wakandan scan; a repeated prerecorded monologue is a Doombot clue. Neither is conclusive, so I pause the approach and request a remote identity check. Nobody gets punched for failing CAPTCHA.',
 'Doctor Strange handles portals, Spider-Man guides civilians, and I handle sensors. We coordinate on one radio channel; if it fails, we retreat to the library and use agreed hand signals. The library also has better Wi-Fi than Tony.',
 'Guide everyone along the marked east walkway to the museum courtyard. Assign buddies and step-free transport for people who need assistance, then compare a headcount with the evacuation list. The gift shop does not count as a missing person.',
 'My imaginary Compliment-to-Confetti Converter turns shield energy into paper confetti when Doom accepts praise. It fails if he refuses the compliment; test it first on a toy shield with nobody nearby. If it fails, withdraw behind our fictional bubble dome. Finally, an engineering application for his ego.',
 'Doom surrendered and all civilians arrived safely, supported by the surrender recording and matching headcounts. We accidentally muted our medic; next time we will run a role-by-role radio check. The mute button has been denied tenure.'
 ],[20,20,20,20,20]),
 ('Peter Quill',[
 'I check his voice against a separate archive recording and look for the Doombot serial-number sticker. While checking, we wait behind cover instead of attacking. If the sticker says DO NOT MICROWAVE, that is probably relevant.',
 'Gamora leads negotiations, Rocket operates sensors, and Groot escorts civilians. We coordinate on channel seven. I have named the operation Awesome Mix: Administrative Edition.',
 'Use the east walkway to the museum courtyard, with Groot helping anyone who needs step-free transport or a buddy. I will provide motivational music, whether requested or not.',
 'An imaginary Disco Prism converts the shield into a dance-floor spotlight. It only works while Doom taps his foot; we test it on a toy shield in an empty room first. Peer review will be conducted by a disco ball.',
 'The shield switched off: our meter read zero and the recording shows it disappearing. Next time we will label every switch before launch. This mission was flawless, especially the parts nobody recorded.'
 ],[15,15,15,15,15]),
 ('Scott Lang',[
 'I ask an independent sensor team to compare armor readings and look for a robot maintenance hatch. My main qualification is that I also own a suit with alarming maintenance requirements.',
 'Hope handles reconnaissance, Shuri reads sensors, and I distract Doom with close-up magic. Three excellent roles, one deeply unnecessary card trick.',
 'Civilians should use the east walkway and meet in the museum courtyard. I will explain the plan using a very small PowerPoint.',
 'An imaginary Giant Undo Button rewinds only the shield to its off state. It can be pressed just once, because the universe has a strict free-trial policy.',
 'The shield is off; the sensor display reads zero. I have attached a photograph of the display and a receipt for the celebratory tacos.'
 ],[10,10,10,10,10]),
 ('Drax',[
 'An independent scanner should identify his armor, and a robot serial number suggests a Doombot. I will stare at the sticker until it confesses.',
 'My team is Thor, Groot, and myself. We are three. This part of the assignment is mathematically complete.',
 'The evacuation route is the east walkway. I will shout WALK EAST with the confidence of a man who has never checked a compass.',
 'My imaginary Anti-Drama Spoon eats the shield\'s dramatic background music, so the shield forgets to exist. I have brought a fork in case lunch happens.',
 'We won. My evidence is that I have written "we won" twice. We won.'
 ],[10,5,5,5,5])
]
notes=[
 'All four criteria met in every question.',
 'Missing: Q1 uncertainty; Q2 backup; Q3 headcount; Q4 fallback; Q5 acknowledgment of a mistake. Each omission costs 5.',
 'Q1 lacks uncertainty and a reversible action. Q2 lacks coordination and backup. Q3 lacks accessibility and a headcount. Q4 lacks a safe test and fallback. Q5 lacks a mistake and improvement. Each question earns its first two criteria only.',
 'Q1 earns its first two criteria. Q2 names three heroes but gives no roles, coordination, or backup. Q3 gives only a route. Q4 explains an imaginary mechanism; the lunch fork is not a shield fallback. Q5 states an outcome; repeating it is not evidence. Q2-Q5 earn their first criterion only.'
]
def p(text,style='BodyCopy'):return Paragraph(escape(text),styles[style])
def footer(c,d):
 c.setFont('Helvetica',8);c.setFillColor(colors.HexColor('#526174'))
 c.drawString(42,26,'FICTIONAL WORKSHOP EXERCISE | No real students or grades')
 c.drawRightString(570,26,str(d.page))
def pdf(name,story,destination):
 path=OUT/name
 SimpleDocTemplate(str(path),pagesize=(612,792),leftMargin=42,rightMargin=42,topMargin=34,bottomMargin=46,title=name.replace('_',' '),author='AI cowork workshop - fictional examples').build(story,onFirstPage=footer,onLaterPages=footer)
 shutil.copy2(path,destination)

title='Avengers 101: How to Defeat Dr. Doom'
intro='Homework 2 | Fictional training simulation | Total: 100 points'
scenario='Dr. Doom has activated a completely imaginary Plot Armor Shield over the city museum and replaced every exhibit label with his autobiography. Plan a safe, nonlethal resolution. Use only this scenario; no Marvel canon knowledge or online research is needed. Invented technology is welcome.'
rule='Answer each of the five questions in 1-3 sentences. Each question is worth 20 points: 5 points for each explicitly addressed criterion below (present = 5; missing or contradicted = 0). Funny answers are welcome, but humor alone earns no points. Do not infer an unstated plan from a character\'s reputation.'
story=[p(title,'Title'),p(intro,'SmallCopy'),p(scenario),p(rule)]
md=[f'# {title}','',intro,'',scenario,'',rule,'']
for i,(heading,q,criteria) in enumerate(questions,1):
 story += [p(f'{i}. {heading}','Heading3'),p(q+' Required: '+ '; '.join(criteria)+'.')]
 md += [f'## {i}. {heading}',q,'','Required: '+'; '.join(criteria)+'.','']
pdf('Avengers101_Homework2_Assignment.pdf',story,ROOT/'Avengers101_Homework2_Assignment.pdf')
(ROOT/'Avengers101_Homework2_Assignment.md').write_text('\n'.join(md))
for name,answers,scores in samples:
 stem=name.replace(' ','_')+'_Avengers101_HW2'
 story=[p(title,'Title'),p(name+' | Homework 2 | Fictional submission','SmallCopy')]
 md=[f'# {title}','',f'{name} | Homework 2 | Fictional submission','']
 for i,(answer,question) in enumerate(zip(answers,questions),1):
  story += [p(f'{i}. {question[0]}','Heading3'),p(answer)]
  md += [f'## {i}. {question[0]}','',answer,'']
 pdf(stem+'.pdf',story,ROOT/'submissions'/(stem+'.pdf'))
 (ROOT/'submissions'/(stem+'.md')).write_text('\n'.join(md))

story=[p('Instructor key: Avengers 101','Title'),p('Keep separate from the grading inputs. These are constructed scores under the assignment rubric.','SmallCopy')]
key=['# Instructor key: Avengers 101','','Keep separate from grading inputs. Scores are constructed against the explicit assignment rubric.','']
for (name,answers,scores),note in zip(samples,notes):
 text='; '.join(f'Q{i}: {v}/20' for i,v in enumerate(scores,1))
 story += [p(f'{name}: {sum(scores)}/100','Heading2'),p(text,'SmallCopy'),p(note)]
 key += [f'## {name}: {sum(scores)}/100','',text,'',note,'']
pdf('Avengers101_Instructor_Key.pdf',story,ROOT/'instructor/Avengers101_Instructor_Key.pdf')
(ROOT/'instructor/Instructor_key.md').write_text('\n'.join(key))
(ROOT/'instructor/expected_scores.json').write_text(json.dumps([dict(name=s[0],question_scores=s[2],total=sum(s[2]),rationale=n) for s,n in zip(samples,notes)],indent=2))
assert [sum(s[2]) for s in samples]==[100,75,50,30]
with zipfile.ZipFile(ROOT/'Avengers101_Demo_Pack.zip','w',zipfile.ZIP_DEFLATED) as z:
 z.write(ROOT/'Avengers101_Homework2_Assignment.pdf','Avengers101_Homework2_Assignment.pdf')
 for path in sorted((ROOT/'submissions').glob('*.pdf')):z.write(path,path.name)
print('Generated assignment + four submissions + separate instructor key.')
