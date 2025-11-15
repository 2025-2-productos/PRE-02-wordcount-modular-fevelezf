import os


def test_migracion():

    if not os.path.exists("data/input/"):
        raise FileNotFoundError(
            "El archivo results.tsv no existe. Por favor, asegúrate de ejecutar el script wordcount.py para generar los datos necesarios."
        )

    results = {}

    with open("data/output/results.tsv", "r", encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines:
        key, value = line.strip().split("\t")
        results[key] = int(value)

    assert results.get("computational", 0) == 3
    assert results.get("analytics", 0) == 5
