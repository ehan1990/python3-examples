import json


def main():
    with open("file.json") as f:
        data = json.loads(f.read())
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
