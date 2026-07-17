import json


with open(
    "evaluation/prompt_test_cases.json"
) as file:

    tests=json.load(file)



for test in tests:

    print(
        "Question:",
        test["question"]
    )

    print(
        "Expected:",
        test["expected"]
    )

    print("----------------")