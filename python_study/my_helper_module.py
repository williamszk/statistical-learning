import json

def printdict(my_dict):
    print(
        json.dumps(
            my_dict,
            indent=4
        )
        )


