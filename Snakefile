conda: "environment.yml"

rule plot:
    input: "data/output/Results.csv"
    output:
        "data/output/plots/zci-diff-hist.png",
        "data/output/plots/zcv-diff-hist.png",
        "data/output/plots/zc-tmy.png",
    notebook: "notebooks/graficas.ipynb"

rule select_input:
    input: "data/ign/MUNICIPIOS.csv"
    output: "data/output/Municipios.csv"
    script: "src/select_input.py"

rule download_data:
    input: "data/output/Municipios.csv"
    output: "data/output/downloads_done.txt"
    shell: "python3 src/download_TMY.py && touch data/output/downloads_done.txt"

rule compute_indicators:
    input: "data/output/Municipios.csv", "data/output/downloads_done.txt"
    output: "data/output/Results.csv"
    script: "src/compute_indicators.py"
