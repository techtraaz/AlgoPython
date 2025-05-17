#naive string matching algo

def naive_string_matcher(T, P):
    n = len(T)
    m = len(P)
    # start from 0 index 
    for s in range(n - m + 1):
        if T[s:s + m] == P:
            print(f"Pattern occurs with shift {s}")


T = "abcxabcdabcdabcy"
P = "abc"
naive_string_matcher(T, P)

