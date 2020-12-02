from rna_tools.SecondaryStructure import draw_ss
import argparse
import os


def linear_representation(sequence, structure):
    ans = ["." for _ in range(len(sequence))]
    for s in structure:
        ans[min(s) - 1] = "("
        ans[max(s) - 1] = ")"
    return "".join(ans)


parser = argparse.ArgumentParser(description='RNA Secondary Structure Predicion')
parser.add_argument('--input', type=str, required=True, help='ct file input')
args = parser.parse_args()
input = args.input
seq = ''
structs = []

with open(input) as f:
    first_line = f.readline()
    length, name = first_line.split()
    length = int(length)
    for line in f:
        link1, nu, dummy, dummy2, link2, dummy3 = line.split()
        if int(link1) != 0 and int(link2) != 0 and int(link1) < int(link2):
            structs.append((int(link1), int(link2)))
        seq += nu
print(linear_representation(seq, structs))
if not os.path.exists('compare/{}'.format(name)):
    os.mkdir('compare/{}'.format(name))
draw_ss(name, seq, linear_representation(seq, structs), 'compare/{}/real.png'.format(name))
os.system('python main.py --seq {} --output compare/{}/nussinov_1.png --min_loop_length 1'.format(seq, name))
os.system('python main.py --seq {} --output compare/{}/nussinov_3.png --min_loop_length 3'.format(seq, name))
os.system('python main.py --seq {} --output compare/{}/nussinov_5.png --min_loop_length 5'.format(seq, name))
os.system('python main.py --seq {} --output compare/{}/nussinov_10.png --min_loop_length 10'.format(seq, name))
os.system('python zuker.py --seq {} --output compare/{}/zuker.png'.format(seq, name))

