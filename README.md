# Thin-triangle Kakeya problem, N = 128: union area 0.106909263576018

An exact certificate for a slightly smaller union of 128 thin triangles than the best value I could find
(0.106909326997687, certified 2026-10-22). Unrefereed. It is a refinement of that earlier construction, not a new method.

## What's here
- `certificate.json`: the 128 intercepts as integers over 2^40, and the exact area as a fraction.
- `verify.py`: exact checker, Python standard library only.
- `ISSUE.md`: the claim as posted, with the comparison table, credit and AI-use statement.
- `SHA256SUMS`: digests of the certificate and the verifier.

## How to check it
    python3 verify.py certificate.json

It recomputes the area in exact rational arithmetic and prints whether it matches the certificate and whether it is
below the 2026-10-22 value. It takes a few seconds.

## Result
| Construction | Union area |
| --- | --- |
| Keich (1999), n = 7 | 0.119207265425702 |
| AlphaEvolve (2025) | 0.114810325818618 |
| kakeya-records (2026-10-22) | 0.106909326997687 |
| This certificate | 0.106909263576018 |

Margin: 6.342e-8.

## Sources and credit
- Starting construction: https://github.com/shrestha-droid/kakeya-records (results/n128.json). This certificate polishes it.
- Problem statement and validator: https://github.com/ewang26/HorizonMath (problem `keich_thin_triangles_128`).
- Earlier construction: https://github.com/google-deepmind/alphaevolve_repository_of_problems (Kakeya needle experiments).
- U. Keich, "On L^p bounds for Kakeya maximal functions and the Minkowski dimension in R^2" (1999), Theorem 1.

## AI use
Found and checked by Claude (Anthropic) under my direction. No human mathematician has reviewed it and no second
party has replayed it.
