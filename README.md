🧬 CRISPR-Cas9 In-Silico Analysis
A beginner-level bioinformatics project that computationally simulates the CRISPR-Cas9 gene editing mechanism using Python. This project was developed as part of a mini research report exploring how guide RNA (sgRNA) is designed, how it binds to a target DNA sequence, and how GC content influences editing efficiency.

📁 Repository Structure
crispr-cas9-insilico-analysis/
├── crispr_analysis.py        # Main Python script
├── README.md                 # Project overview (this file)
├── requirements.txt          # Python dependencies
├── report/
│   └── CRISPR_Cas9_InSilico_Research_Report.docx
└── results/
    └── output.txt            # Script output

🔬 What This Project Does
Given a target DNA sequence, the script:

Generates the complementary DNA strand using Watson-Crick base pairing (A↔T, G↔C)
Transcribes the complementary strand into guide RNA (replaces T with U)
Simulates target recognition by matching the guide RNA against the target
Calculates GC content — a key indicator of guide RNA stability and editing efficiency


🧪 Sample Input & Output
Input DNA:
ATGCGTACGTTAGCTAGCTAGGCTA
Output:
=== CRISPR-Cas9 In-Silico Analysis ===

Original DNA Sequence:
ATGCGTACGTTAGCTAGCTAGGCTA

Complementary DNA Sequence:
TACGCATGCAATCGATCGATCCGAT

Guide RNA Sequence:
UACGCAUGCAAUCGAUCGAUCCGAU

Guide RNA partially matched target region.

GC Content: 48.00%

▶️ How to Run
1. Clone the repository
bashgit clone https://github.com/Karthiga-M-CSE/IN-SILICO-ANALYSIS-OF-CRISPR-Cas9-GENE-EDITING-MECHANISM.git
cd crispr-cas9-insilico-analysis
2. (Optional) Install dependencies
bashpip install -r requirements.txt
3. Run the script
bashpython crispr_analysis.py

🛠️ Requirements

Python 3.x
Biopython (optional — script uses pure Python logic)

Install with:
bashpip install biopython
Or use the included requirements.txt:
bashpip install -r requirements.txt


📬 Author
Developed as a mini research project in Computational Bioinformatics.
