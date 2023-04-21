# Fasta to Prey Converter
The "Fasta to Prey Converter" is a Streamlit app that converts a FASTA file of protein sequences into a prey file.

## Try Online
https://fasta-to-prey.streamlit.app/

## Installation
1) Clone or download the repository containing the app files.
2) Open a terminal or command prompt and navigate to the directory where the repository is located.
3) Install the required Python packages by running the following command: pip install -r requirements.txt

## Usage
1) Run the app by running the following command: streamlit run app.py
2) Once the app is running, click the "Choose a .fasta file" button to upload a FASTA file containing protein sequences.
3) After selecting the file, click the "Run" button to process the file.
4) If there are any warnings, they will be displayed in the "Warnings" section of the app.
5) If valid prey file content is found in the input file, the app will display a "Download Prey File" button. Click this button to download the prey file in tab-separated format.
