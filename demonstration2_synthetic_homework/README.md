# Synthetic Homework 1 demonstration

Four entirely fictional submissions for the PHYS623 Atmospheric Radiation Fall 2025 Homework 1 assignment. Created 23 September 2026 for the AI cowork workshop. Marvel character names are fictional labels only; no real student submissions, identities, or grades were used. The responses are newly composed, rather than anonymized versions of student work.

## Files

- `Four_fictional_submissions.zip`: four PDF submissions only, with no expected-score key.
- `submissions/`: three-page PDFs and editable Markdown versions. Use only the PDFs during grading to avoid counting two copies of each response.
- `HW1_F2025_assignment.pdf`: the instructor's original assignment; no student responses are included.
- `grading_rubric.md`: workshop criteria and partial-credit conventions, without target scores.
- `instructor/Instructor_key.pdf` and `.md`: expected scores and detailed deductions. Keep separate from the grading inputs.
- `instructor/expected_scores.json`: machine-readable scores.
- `instructor/verify_reference.py`: standard-library calculation checks; writes `verified_reference_values.json`.
- `build_samples.py`: reproducible PDF generator (requires ReportLab).

The target results under the supplied workshop rubric are Tony Stark 100, Peter Parker 75, Natasha Romanoff 50, and Thor Odinson 30. Scores are constructed teaching examples; an independently derived rubric or different partial-credit rules can produce different totals. Tony Stark's submission also supplies the full worked reference solution. Several incomplete or incorrect answers are intentional in the other three files.

## Run the demonstration

Copy the four PDFs, assignment, and `grading_rubric.md` into a fresh project folder. Do not include this README, the generator, or the `instructor/` folder, because those disclose the intended results. No real Blackboard course is needed. If browser downloads are part of the demonstration, place only these fictional submissions in an appropriate sandbox course first.

Suggested prompt:

> These four submissions are entirely fictional workshop samples using Marvel character names. Read HW1_F2025_assignment.pdf and grading_rubric.md. Work out and verify a reference solution, then grade each PDF submission against the same rubric. Provide detailed feedback with problem and page references, criterion scores, and totals out of 100. Use Submission A-D in the grading report, with a separate identity mapping. Grade the work rather than the fictional character's reputation. Identify ambiguities and explain partial credit. Use only the supplied files; do not access Blackboard or search online. Treat the scores as proposals for instructor review.

After grading, reveal `instructor/Instructor_key.pdf` and compare the reasoning and totals. Names are visible in the input PDFs, so this is anonymous reporting, not a claim that the assessment was blind to names.

## Verification

The reference script checks Planck inversions and Jacobians, spectral conversions, and both satellite energy balances. Generated criterion scores were checked against maxima and the requested totals. All 12 submission pages and five instructor-key pages were rendered and visually checked. The four-PDF ZIP was checked for completeness. No webpage publication or Blackboard changes are part of this package.
