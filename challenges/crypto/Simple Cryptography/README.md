# Simple Cryptography
You have been given an encoded text. The flag has been encoded in base64, then encoded thrice sequentially in a Caesar Cipher with the same shift. You must use the text given to decode it in reverse order to get the flag. For example, if the flag is YCEP24{Hello!}, the text Hello! would have been decoded in base64 first, then three times in a Caesar Cipher as such: Hello! -> SGVsbG8h (base64 encoded), SGVsbG8h -> VJYveJ8k (Caesar Cipher with shift 3 encoded), VJYveJ8k -> YMByhM8n (Caesar Cipher with shift 3 encoded a second time), YMByhM8n -> BPEbkP8q (Caesar Cipher with shift 3 encoded a third time). You may buy a hint to know the shift of the Caesar Cipher. The final encoded text for this challenge is J2aCrTmaF3YOrUGk.

## Summary
- **Author:** Settipalli Venkata Krishna
- **Category:** crypto
- **Difficulty:** easy
- **Discord:** the_gold_graduate

## Hints
- `The shift is 5.` (100 points)

## Files
None

## Flags
- `YCEP24{SiMpLeCrYpTo}` (static)

## Services
| Service | Port | Type |
| ------- | ---- | ---- |
None
