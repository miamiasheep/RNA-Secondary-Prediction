import numpy as np
import argparse
from rna_tools.SecondaryStructure import draw_ss


def initialize(n):
    return np.zeros((n, n))


scores = {
            ('A', 'U'): 1,
            ('C', 'G'): 1
}

pairs = set([('A', 'U'), ('C', 'G')])


def is_pair(tup):
    if tup in pairs or tup[::-1] in pairs:
        return True
    return False


def get_scores(tup):
    if tup in scores:
        return scores[tup]
    if tup[::-1] in scores:
        return scores[tup[::-1]]
    return 0


def traceback(i, j):
    if j <= i:
        return
    elif dp[i][j] == dp[i][j-1]:
        traceback(i, j-1)
    else:
        for k in [b for b in range(i, j - min_loop_length) if is_pair((seq[b], seq[j]))]:
            if k-1 < 0:
                if dp[i][j] == dp[k+1][j-1] + 1:
                    structure.append((k, j))
                    traceback(k+1, j-1)
                    traceback(i, k-1)
                    break
            elif dp[i][j] == dp[i][k-1] + dp[k+1][j-1] + 1:
                structure.append((k, j))
                traceback(i, k-1)
                traceback(k+1, j-1)
                break


def linear_representation(sequence, structure):
    ans = ["." for _ in range(len(sequence))]
    for s in structure:
        ans[min(s)] = "("
        ans[max(s)] = ")"
    return "".join(ans)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description= 'RNA Secondary Structure Predicion')
    parser.add_argument('--seq', type=str, default='CGAGUCGGAGUC', help='RNA sequence')
    parser.add_argument('--output', type=str, default='demo.png', help='The output path of images of predicted secondary struction')
    parser.add_argument('--min_loop_length', type=int, default=0, help='min loop length')
    args = parser.parse_args()
    seq = args.seq
    min_loop_length = args.min_loop_length
    n = len(seq)
    dp = initialize(n)

    # fill in the dp array diagnally
    for k in range(n):
        for i in range(n - k):
            j = i + k
            if i >= j:
                dp[i][j] = 0
            else:
                opts = [dp[i][j - 1]]
                for t in range(i, j - min_loop_length):
                    if is_pair((seq[t], seq[j])):
                        opts.append(1 + dp[i][t - 1] + dp[t + 1][j - 1])
                opts.append(0)
                dp[i][j] = max(opts)
    # trace back
    print(dp)
    structure = []
    traceback(0, n-1)
    linear_resp = linear_representation(seq, structure)
    print(linear_resp)
    draw_ss('', seq, linear_resp, args.output)
