import json


files = [
    "training_data.jsonl",
    "validation_data.jsonl"
]


for file in files:

    path = f"fine_tuning/{file}"

    print(
        f"\nChecking {file}"
    )


    with open(path,"r") as f:

        lines=f.readlines()


    for index,line in enumerate(lines):

        try:

            data=json.loads(line)


            if "messages" not in data:

                print(
                    f"Missing messages at line {index+1}"
                )


        except Exception as e:

            print(
                f"Invalid JSON line {index+1}",
                e
            )


    print(
        "Validation completed"
    )