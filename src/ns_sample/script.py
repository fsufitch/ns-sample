import sys
from ns_sample.storage import ThingStorage

def main():
    if len(sys.argv)<2:
        print("Please specify an input file")
        return

    infile = sys.argv[1]
    storage = ThingStorage()
    with open(infile) as f:
        storage.parse_file(f)

    storage.output_categories()
    storage.output_pairs()
