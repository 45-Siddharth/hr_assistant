import json

with open(
    "evaluation/baseline_results.json",
    "r"
) as file:

    baseline = json.load(file)

with open(
    "evaluation/finetuned_results.json",
    "r"
) as file:

    finetuned = json.load(file)

for base, ft in zip(baseline, finetuned):

    print("="*70)

    print("Question:")

    print(base["question"])

    print()

    print("Baseline:")

    print(base["answer"])

    print()

    print("Fine-Tuned:")

    print(ft["answer"])

    print()