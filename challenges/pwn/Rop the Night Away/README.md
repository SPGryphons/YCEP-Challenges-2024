# Rop the Night Away
i heard that if you're able to leak a function from libc, you can ret2libc~

## Summary
- **Author:** gatari
- **Category:** pwn
- **Difficulty:** insane
- **Discord:** gatari

## Hints
None

## Files
- [ld-linux-x86-64.so.2](dist/ld-linux-x86-64.so.2)
- [libc.so.6](dist/libc.so.6)
- [rop_the_night_away.zip](dist/rop_the_night_away.zip)

## Flags
- `YCEP24{roP_7hE_N!6HT_Aw@Y_30f9b33fc4087aea8ffeff202003e91c}` (static)

## Services
| Service | Port | Type |
| ------- | ---- | ---- |
| [`rop_the_night_away`](service/rop_the_night_away) | 5000 | nc |
