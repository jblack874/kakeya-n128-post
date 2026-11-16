**Title:** Thin-triangle Kakeya, N = 128: union area 0.106909263576018 (6.3e-8 below 0.106909326997687)

A small refinement of the N = 128 construction in this repository (n128.json, certified 2026-10-22).

| Construction | Union area |
| --- | --- |
| Keich (1999), n = 7 | 0.119207265425702 |
| AlphaEvolve (2025) | 0.114810325818618 |
| kakeya-records (2026-10-22) | 0.106909326997687 |
| This certificate | **0.106909263576018** |

- **Exact value:** 144650770862078211201996129247 / 1353023732683594899185278648320, for intercepts b_i = B_i / 2^40.
- **Margin:** 6.342e-8 below the 2026-10-22 value.
- **How:** started from your n128 intercepts; gradient descent on the union area with random restarts, 95 seconds on 2 cores; intercepts rounded to multiples of 2^-40; area then computed exactly.
- **Check:** `python3 verify.py certificate.json` (standard library only, exact rational arithmetic over every breakpoint in x). The HorizonMath validator `validators.keich_thin_triangles_128` returns valid=True, area = 0.106909263576018.
- **Credit:** this is your construction, polished. No new method is claimed.
- **AI use:** found and checked by Claude (Anthropic) under my direction. No human mathematician has reviewed it and no second party has replayed it.
- **Not checked:** values posted elsewhere after 2026-10-23 that my search did not find.

Files: https://github.com/jblack874/kakeya-n128-post
