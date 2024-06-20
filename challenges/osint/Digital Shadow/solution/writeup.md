# Solution

1. Browse `https://docs.google.com/document/d/143hKqSdb6jnM6ZGb58VBff4dnXDvKa9PTTm4WcPO-sk/edit?usp=sharing`.

    `I found his username “kiraisha” and the repo name is “t-hacker007” but we don’t have access. Can you break in?`

2. Visit `https://github.com/kiraisha/note.`

3. `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` Get this in the secret file at line 500.

4. Run this command to get the private repo.
   `git clone https://kiraisha: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@github.com/kiraisha/t-hacker007.git`

5. One of the commit contains `WUNFUDI0e20xc3MxME5fMTNfQzBtcDFldDNEX3NoM3NofQ==`

6. Decode this using base64.

Flag: `YCEP24{m1ss10N_13_C0mp1et3D_sh3sh}`
