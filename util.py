import re
from Bio import SeqIO


def read_file(fasta_file_path):
    records = []
    for record in SeqIO.parse(fasta_file_path, "fasta"):
        records.append(record)
    records_dict = {i: record for i, record in enumerate(records)}
    return records_dict


def extract_os(input_string):
    os_pattern = r'OS=([\w\s]+)\s'
    match = re.search(os_pattern, input_string)
    if match:
        return match.group(1)
    else:
        raise ValueError("OS not found")


def extract_ox(input_string):
    ox_pattern = r'OX=([\w\s]+)\s'
    match = re.search(ox_pattern, input_string)
    if match:
        return match.group(1)
    else:
        raise ValueError("OX not found")


def extract_gn(input_string):
    gn_pattern = r'GN=([\w-]+)\s'
    match = re.search(gn_pattern, input_string)
    if match:
        return match.group(1)
    else:
        raise ValueError("GN not found")


def extract_pe(input_string):
    pe_pattern = r'PE=(\d+)'
    match = re.search(pe_pattern, input_string)
    if match:
        return int(match.group(1))
    else:
        raise ValueError("PE not found")


def extract_sv(input_string):
    sv_pattern = r'SV=(\d+)'
    match = re.search(sv_pattern, input_string)
    if match:
        return int(match.group(1))
    else:
        raise ValueError("SV not found")
