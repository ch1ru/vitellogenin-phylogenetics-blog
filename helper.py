import requests
import json
import sys
import os
from Bio.SeqIO import parse

base_url = 'https://rest.ensembl.org/'

def get_ensembl_id(species: str, symbol: str):
    symbol_url = base_url + f"xrefs/symbol/{species}/{symbol}"
    resp = requests.get(
      url=symbol_url, 
      headers={ "Content-Type" : "application/json"}
    )
    if not resp.ok:
        resp.raise_for_status()
        sys.exit()
    decoded = resp.content.decode()
    return json.loads(decoded)[0]['id']

def get_sequence_from_id(id: str):
    seq_url = base_url + f"sequence/id/{id}"
    resp = requests.get(
      url=seq_url, 
      headers={ "Content-Type" : "text/plain"}
    )
    if not resp.ok:
        resp.raise_for_status()
        sys.exit()
    seq = resp.content.decode()
    return seq

def write_to_file(seq: str, species: str, gene: str):
    if not os.path.isdir(f'{species}'):
        os.mkdir(f'{species}')

    with open(os.path.join(f'{species}', f'{gene}.fasta'), mode='w') as f:
        f.write(f">{species}:{gene}\n{seq}")

