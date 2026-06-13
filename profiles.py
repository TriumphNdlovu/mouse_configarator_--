import json

PROFILE_PATH = "profiles/default.json"

def load_profile():
    with open(PROFILE_PATH, "r") as file:
        return json.load(file)

def save_profile(profile_data):
    with open(PROFILE_PATH, "w") as file:
        json.dump(profile_data, file, indent=4)