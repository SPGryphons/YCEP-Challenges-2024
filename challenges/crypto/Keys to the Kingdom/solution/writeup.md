To solve the challenge it would require you to be able to understand
that n is prime a quick google search would produce this with reference
to rsa when n is prime

I then found an article and it then says this

It then explains this at the end of the article this

[The totient ϕ 𝜙 of a prime number N 𝑁 is trivial to calculate as all
integers less than N]{.mark}

[𝑁 are co-prime with N 𝑁, hence ϕ(N)=N−1 𝜙(𝑁)=𝑁−1. Once we know ϕ(N)=N−1
𝜙(𝑁)=𝑁−1 we can easily recover the private key d 𝑑 from the public key
(e,N) (𝑒,𝑁), we just calculate d=e−1 mod (N−1)]{.mark}

[𝑑=𝑒−1 mod (𝑁−1).]{.mark}

So all we need to do is to calculate the [ϕ(N) which would help us get
the private key for us to decrypt the flag which when we run it with the
solve script which decrypts it using this formula as per rsa]{.mark}

[m=c\^d (mod n)]{.mark}

[We get]{.mark}

[FLAG:]{.mark}![](./image1.png){width="5.791666666666667in"
height="0.28125in"}

[YCEP24{S0_y0u_h@ve_f0und_a_w@y_t0_n0t_U\$e_K3ys}]{.mark}
