"""Exact check of certificate.json for the thin-triangle Kakeya problem, N = 128.
Standard library only.   Usage: python3 verify.py certificate.json

Intercepts are b_i = B_i / 2^40. Slopes a_i = i/128, delta = 1/128. At each x in [0,1] triangle i has
cross-section [a_i x + b_i - delta(1-x), a_i x + b_i]. All cross-sections at a given x have the same length
w = delta(1-x), so with the upper endpoints sorted the union length is w + sum_k min(w, gap_k).
That length is piecewise linear in x. Breakpoints: two upper endpoints cross, or a gap equals w.
The trapezoid rule between consecutive breakpoints is therefore exact.
"""
import json, sys
from fractions import Fraction
N = 128; Q2 = 1 << 40
c = json.load(open(sys.argv[1])); B = [int(v) for v in c['intercepts_times_2^40']]
assert len(B) == N
xs = set()
for i in range(N):
    for j in range(i + 1, N):
        num = 128 * (B[i] - B[j]); den = Q2 * (j - i)
        if 0 < num < den: xs.add(Fraction(num, den))
for i in range(N):
    for j in range(N):
        m = i - j + 1
        if i == j or m == 0: continue
        num = Q2 - 128 * (B[i] - B[j]); den = Q2 * m
        if den < 0: num, den = -num, -den
        if 0 < num < den: xs.add(Fraction(num, den))
pts = [Fraction(0)] + sorted(xs) + [Fraction(1)]
def length(xf):
    P, Q = xf.numerator, xf.denominator
    U = sorted(i * P * Q2 + B[i] * 128 * Q for i in range(N)); w = (Q - P) * Q2; tot = w
    for k in range(1, N):
        g = U[k] - U[k - 1]; tot += g if g < w else w
    return Fraction(tot, 128 * Q * Q2)
area = Fraction(0); px = pts[0]; pl = length(px)
for xf in pts[1:]:
    l = length(xf); area += (xf - px) * (pl + l) / 2; px, pl = xf, l
claimed = Fraction(int(c['area_numerator']), int(c['area_denominator']))
print('breakpoints:', len(pts)); print('exact area:', area.numerator, '/', area.denominator); print('= %.18f' % float(area))
print('matches the certificate:', area == claimed)
print('below 0.106909326997687 (kakeya-records, 2026-10-22):', area < Fraction(106909326997687, 10**15))
