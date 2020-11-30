from seqfold import dg, dg_cache, fold, Struct
from rna_tools.SecondaryStructure import draw_ss
import argparse


def linear_representation(sequence, structure):
    ans = ["." for _ in range(len(sequence))]
    for s in structure:
        ans[min(s)] = "("
        ans[max(s)] = ")"
    return "".join(ans)


parser = argparse.ArgumentParser(description= 'RNA Secondary Structure Predicion')
parser.add_argument('--seq', type=str, default='CGAGUCGGAGUC', help='RNA sequence')
parser.add_argument('--output', type=str, default='zucker.png', help='The output path of images of predicted secondary struction')
args = parser.parse_args()
output = args.output
seq = args.seq

structs = fold(seq)
ij_structs = []
for struct in structs:
    ij_structs.append(struct.ij[0])

print(linear_representation(seq, ij_structs))
draw_ss('RNA', seq, linear_representation(seq, ij_structs), output)

