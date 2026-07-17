from pathlib import Path


def load_prompt(version="v3"):

    file_path = Path(
        f"prompts/system_prompt_{version}.txt"
    )

    with open(file_path,"r") as file:
        return file.read()