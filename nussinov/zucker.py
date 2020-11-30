from seqfold import dg, dg_cache, fold, Struct
from rna_tools.SecondaryStructure import draw_ss
import argparse
import matplotlib.pyplot as plt
import networkx as nx


def linear_representation(sequence, structure):
    ans = ["." for _ in range(len(sequence))]
    for s in structure:
        ans[min(s)] = "("
        ans[max(s)] = ")"
    return "".join(ans)


parser = argparse.ArgumentParser(description= 'RNA Secondary Structure Predicion')
parser.add_argument('--seq', type=str, default='CGAGUCGGAGUC', help='RNA sequence')
parser.add_argument('--output', type=str, default='zucker.png', help='The output path of images of predicted secondary struction')
parser.add_argument('--seq_file', type=str, default=None, help='File for RNA Sequence')
parser.add_argument('--circular_plot_file', type=str, default=None, help='The output path of circular plot')
args = parser.parse_args()
output = args.output
seq = args.seq
seq_file = args.seq_file
circular_plot_file = args.circular_plot_file
if seq_file is not None:
    seq = open(seq_file).readline()
n = len(seq)
structs = fold(seq)
ij_structs = []
for struct in structs:
    ij_structs.append(struct.ij[0])

print(linear_representation(seq, ij_structs))
draw_ss('RNA', seq, linear_representation(seq, ij_structs), output)

if circular_plot_file is not None:
    G = nx.Graph()
    for i in range(1, n):
        G.add_edge(i - 1, i)
    labels = {}
    for i in range(n):
        labels[i] = seq[i]
    for i, j in ij_structs:
        G.add_edge(i, j)
    pos = nx.circular_layout(G)
    nx.draw(G, pos, labels=labels, with_labels=True)
    plt.savefig(circular_plot_file)

