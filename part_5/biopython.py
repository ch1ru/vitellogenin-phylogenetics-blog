#!/home/kitsune/miniconda3/envs/vtg-alignment-env/bin/python

from Bio import AlignIO, SeqRecord
from Bio.Seq import Seq 
from Bio.Seq import transcribe, translate
from Bio import Phylo
import argparse

def substitution_matrix():
    print("Substitution matrix:")
    alignment = AlignIO.read(alignment_file, format='clustal')
    print(alignment.substitutions)

def translate_to_aa():
    alignment = AlignIO.read(alignment_file, format='clustal')
    print("Amino acid residues (with stop codons)")
    for aln in alignment:
        seq = Seq(aln.seq).replace('-', '') # remove gaps in alignment
        mRNA = transcribe(seq)
        aa = translate(mRNA) # translate to amino acid sequence
        print(aln.id)
        print(aa)
        print()

def draw_tree():
    print("Clustalw tree")
    tree = Phylo.read(tree_file, "newick")
    Phylo.draw_ascii(tree)

###### ARG parse ######

FUNCTION_MAP = {'substitution_matrix' : substitution_matrix, 'translate_to_aa' : translate_to_aa, 'draw_tree' : draw_tree }

parser = argparse.ArgumentParser(
    prog='biopython',
    description='A simple script to demonstrate functionality available within Biopython.',
    epilog='Text at the bottom of help'
)

parser.add_argument('-a', '--alignment', help="Alignment file in clustal format.")
parser.add_argument('-t', '--tree', help="Tree file in Newick format.")
parser.add_argument('command', choices=FUNCTION_MAP.keys())

args = parser.parse_args()

#######################

alignment_file = args.alignment
tree_file = args.tree

func = FUNCTION_MAP[args.command]
func()