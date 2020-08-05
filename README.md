# sif
Python code to generate Stabilized-Interval-Free (SIF) permutations.

This code uses Callan's recursive formula for the enumeration of SIF permutations, see https://arxiv.org/pdf/math/0310157.pdf.

Because the generator stores all SIF permutations of length up to the requested n, you will run out of memory quickly at n>11.
