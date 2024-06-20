# Solution

1. There is a corrupted PNG in the .config folder. Fix the PNG header will show a part of the encrypted text ```1cmVQ```.

2. There is a lot of .txt files in the ```.config/secret/``` folder. Use the command: ```grep 1cmVQ .config/secret/*/*```
* This command will output: ```.config/secret/31/5.txt:CjEyMzRJc0FTZWN1cmVQYXNzd29yZA==```

3. Base64 decode this, we got the password ```1234IsASecurePassword```

4. There is a hint in the Images folder that talks about steghide tool.

5. In the badfiles folder, there are many .jpg images that we can use steghide to extract the message. 
* Using this command for automation: ```ls | while read lines; do steghide extract -sf $lines -p 1234IsASecurePassword; done```

* One of the jpg will output the flag.txt file that contains the flag:
```YCEP24{4ut0m4t10n_1s_7h3_w49_t0_g0_sdfw2ff}```

Flag: ```YCEP24{4ut0m4t10n_1s_7h3_w49_t0_g0_sdfw2ff}```