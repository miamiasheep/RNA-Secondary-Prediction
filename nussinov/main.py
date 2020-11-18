import numpy as np

def initialize(n):
    return np.zeros((n, n))


scores = {
            ('A', 'U'): 1,
            ('C', 'G'): 1
}


def get_scores(tup):
    if tup in scores:
        return scores[tup]
    if tup[::-1] in scores:
        return scores[tup[::-1]]
    return 0


if __name__ == '__main__':
    seq = 'CGAGUCGGAGUC'
    n = len(seq)
    dp = initialize(n)
    print(dp)
    # fill in the dp array
    for k in range(n):
        for i in range(n-k):
            j = i + k
            if i >= j:
                dp[i][j] = 0
            else:
                opts = [dp[i][j-1]]
                for t in range(i, j):
                    opts.append(get_scores((seq[t], seq[j])) + dp[i][t-1] + dp[t+1][j-1])
                opts.append(0)
                dp[i][j] = max(opts)
            # find the optimal solution
    print(dp)
