from io import StringIO

import pandas as pd
import streamlit as st

from util import *

st.title("Fasta to Prey Convertor")

st.markdown("""
The "Fasta to Prey Converter" is a Streamlit app that converts a FASTA file of protein sequences into a prey file.

### Usage
1) click the "Choose a .fasta file" button to upload a FASTA file containing protein sequences.
2) After selecting the file A Run button will appear, click the "Run" button to process the file.
3) If there are any warnings, they will be displayed in the dropdown "Warnings" section of the app.
4) If valid prey file content is found in the input file, the app will display a "Download Prey File" button. 
Click this button to download the prey file in tab-separated format.
""")

uploaded_file = st.file_uploader("Choose a .fasta file", type="fasta")

if uploaded_file is not None:

    if not st.button('Run'):
        st.stop()

    records_dict = read_file(StringIO(uploaded_file.getvalue().decode('utf-8')))

    data = {'unique_identifier': [], 'protein_length': [], 'gene_name': []}

    with st.expander('Conversion Warnings:'):

        prey_lines = []
        for key in records_dict:
            record = records_dict[key]

            # Skip reverse and contaminant record
            if 'Reverse'.casefold() in record.name.casefold() or 'contaminant'.casefold() in record.name.casefold():
                continue

            # Try to parse db, unique_identifier, entry_name from record
            try:
                db, unique_identifier, entry_name = record.name.split('|')
            except ValueError as e:
                st.error(f'Cannot parse db|unique_identifier|entry_name from record.name: {record.name}')
                continue

            gene_name = 'unknown'
            try:
                gene_name = extract_gn(record.description)
            except ValueError as e:
                st.warning(f'Cannot parse GN from protein record.description: {record.description}')

            data['unique_identifier'].append(unique_identifier)
            data['protein_length'].append(len(record.seq))
            data['gene_name'].append(gene_name)

    if len(data['unique_identifier']) > 0:
        st.write("Prey file content generated. Download the prey file below:")
        prey_df = pd.DataFrame(data)

        unique_unique_identifiers = []
        unique_identifier_dict = {}
        for unique_identifier in prey_df['unique_identifier'].values:
            unique_identifier_dict.setdefault(unique_identifier, 0)

            unique_unique_identifier = unique_identifier
            if unique_identifier_dict[unique_identifier] != 0:
                unique_unique_identifier = f'{unique_identifier}-{unique_identifier_dict[unique_identifier]}'

            unique_identifier_dict[unique_identifier] += 1
            unique_unique_identifiers.append(unique_unique_identifier)

        prey_df['unique_identifier'] = unique_unique_identifiers

        st.download_button(label="Download Prey File",
                           data=prey_df.to_csv(sep='\t', header=False, index=False),
                           file_name=f"{uploaded_file.name}.txt",
                           mime="text/plain")
    else:
        st.error("No valid prey file content found.")
else:
    st.info("Please upload a .fasta file.")


