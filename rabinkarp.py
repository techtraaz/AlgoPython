def rabinkarp(pattern,text,d,q):
    m = len(pattern)
    n = len(text)
    h = pow(d,m-1,q)
    phash = 0
    thash = 0

    for i in range(m):
        phash = (d * phash + ord(pattern[i])) % q
        thash = (d * thash + ord(text[i])) % q

    for i in range(n-m+1):
        if phash == thash:
            if text[i:i+m] == pattern:
                print(f"pattern found at index {i}")

        if i < n - m:
            thash = (d * (thash - ord(text[i])*h) + ord(text[i+m])) % q
            if thash < 0:
                thash = thash + q

if __name__ == "__main__":
    text = "ABCCDDAEFG"
    pattern = "CDD"
    rabinkarp(pattern,text,256,101)

