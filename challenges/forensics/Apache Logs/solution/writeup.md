# Solution

1. Analyse the **apache.log** with strings/cat commands.
```
$ strings apache.log
...
179.231.207.73 - - [02/Jun/2024:16:51:11 +0800] "GET /apps/cart.jsp?appID=8862 HTTP/1.0" 200 4993 "https://www.cook.info/categoriesterms.htm" "Mozilla/5.0 (iPad; CPU iPad OS 9_3_6 like Mac OS X) AppleWebKit/535.1 (KHTML, like Gecko) FxiOS/13.5n1334.0 Mobile/19L626 Safari/535.1"
162.0.184.140 - - [02/Jun/2024:16:53:23 +0800] "DELETE /posts/posts/explore HTTP/1.0" 200 4997 "http://www.harris-alexander.org/taglogin.php" "Mozilla/5.0 (X11; Linux x86_64; rv:1.9.6.20) Gecko/7868-05-11 10:19:57 Firefox/3.8"
169.68.52.126 - - [02/Jun/2024:16:56:10 +0800] "GET /apps/cart.jsp?appID=2326 HTTP/1.0" 200 4994 "https://www.cole.com/explore/searchindex.html" "Mozilla/5.0 (Macintosh; PPC Mac OS X 10_11_6; rv:1.9.3.20) Gecko/3962-12-16 06:34:20 Firefox/3.8"
...
```
2. The challenge description will hints us to filter POST and PUT requests.
```
$ strings apache.log | grep 'POST\|PUT'
...
192.125.194.52 - - [03/Jun/2024:06:06:50 +0800] "PUT /explore HTTP/1.0" 200 5018 "http://taylor.com/categorieslogin.php" "Mozilla/5.0 (Windows 98; or-IN; rv:1.9.1.20) Gecko/3171-02-22 21:03:34 Firefox/3.8"
70.116.2.62 - - [03/Jun/2024:06:08:21 +0800] "PUT /apps/cart.jsp?appID=1893 HTTP/1.0" 200 4917 "https://www.powell-mccann.com/postsprivacy.html" "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_12_6 rv:4.0; bg-BG) AppleWebKit/531.17.4 (KHTML, like Gecko) Version/4.0.5 Safari/531.17.4"
55.6.43.84 - - [03/Jun/2024:06:12:24 +0800] "PUT /posts/posts/explore HTTP/1.0" 200 4913 "http://jones.com/listpost.html" "Mozilla/5.0 (Android 6.0; Mobile; rv:61.0) Gecko/61.0 Firefox/61.0"
...
```
3. After some analysis you will see 1 log that indicates a potentially malicious activity.
```
99.102.58.17 - - [03/Jun/2024:02:23:59 +0800] "PUT /css/style.php HTTP/1.0" 200 5122 "https://www.icare.com/" "Mozilla/5.0 (Windows NT 5.1; bs-BA; rv:1.9.2.20) Gecko/3807-10-03 18:20:47 Firefox/3.6.14"
```
4. Therefore the flag is YCEP24{99.102.58.17}

