# toddler pwn
Ever since our ATS system got pwned, my job has been hanging by a thread. Thankfully, someone told me to use fgets() instead of gets() as it is a secure function!

## Summary
- **Author:** gatari
- **Category:** pwn
- **Difficulty:** medium
- **Discord:** gatari

## Hints
None

## Files
- [toddler_pwn.zip](dist/toddler_pwn.zip)
- [vuln.c](dist/vuln.c)

## Flags
- `YCEP24{D@MN_5p_N3eD$_70_$7Ep_Up_th3IR_$ECuRiTy_34b2a76ff7b412cbfc84ab3133eaafb4}` (static)

## Services
| Service | Port | Type |
| ------- | ---- | ---- |
| [`toddler_pwn`](service/toddler_pwn) | 5000 | nc |
