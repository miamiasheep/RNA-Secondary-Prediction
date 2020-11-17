import numpy as np

def initialize(n):
    dp = np.empty((n, n))
    dp[:] = np.NAN
    # fill the dp array with zero
    for i in range(n):
        j = i
        dp[i][j] = 0
    return dp

if __name__ == '__main__':
    dp = initialize(6)
    print(dp)
