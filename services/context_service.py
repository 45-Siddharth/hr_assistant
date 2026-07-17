from pathlib import Path


DOCUMENT_PATH = Path(
    "knowledge/hr_policy.txt"
)



def load_context():

    with open(
        DOCUMENT_PATH,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()



def get_relevant_context(question):

    context = load_context()


    keywords = [
        word.lower()
        for word in question.split()
    ]


    lines = context.split("\n")


    results = []


    for line in lines:

        for keyword in keywords:

            if keyword in line.lower():

                results.append(line)


    return "\n".join(results)