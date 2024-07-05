from helper import *

# Download vtg 1 for chicken

vtg1_ensembl = get_ensembl_id(species="gallus_gallus", symbol="vtg2")

vtg1_seq = get_sequence_from_id(vtg1_ensembl)

write_to_file(seq=vtg1_seq, species="gallus_gallus", gene="vtg2")