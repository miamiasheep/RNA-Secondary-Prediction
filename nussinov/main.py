import numpy as np

def initialize(n):
    return np.zeros((n, n))

def pair_check(tup):
    if tup in [('A', 'U'), ('U', 'A'), ('C', 'G'), ('G', 'C')]:
        return True
    return False

if __name__ == '__main__':
    seq = 'CGAGUCGGAGUC'
    n = len(seq)
    dp = initialize(n)
    print(dp)
    # fill in the dp array
    print('===============\n')
    for k in range(n):
        for i in range(n-k):
            j = i + k
            if i >= j:
                dp[i][j] = 0
            else:
                opts = [dp[i][j-1]]
                for t in range(i, j):
                    if pair_check((seq[t], seq[j])):
                        opts.append(1 + dp[i][t-1] + dp[t+1][j-1])
                opts.append(0)
                print(opts)
                dp[i][j] = max(opts)
            # find the optimal solution
    print(dp)
