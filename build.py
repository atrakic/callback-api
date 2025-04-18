import argparse
import yaml, json

def main():
    parser = argparse.ArgumentParser(
        prog="Yaml2Json converter"
    )
    parser.add_argument("-f", "--file")
    args = parser.parse_args()
    
    with open(args.file) as file:
        outfile = 'openapi.json'
        with open(outfile, 'w') as out:
            json.dump(yaml.safe_load(file), out, indent=2)

if __name__ == "__main__":
    main()
