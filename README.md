# Dynamic Gate Pruning - official implementation

Official implementation of **Dynamic Gate Pruning for Streaming Speech Models**
(Interspeech 2026).

This paper is a follow-up study to Northvale technical report `TR-2026-0413`.
It borrows the sparse gating vocabulary but implements a different method:
gates are pruned at training time by magnitude rather than by the linear
density schedule of sparse gated convolution.

This repository does **not** implement sparse gated convolution and contains no
implementation of the method described in `TR-2026-0413`.
