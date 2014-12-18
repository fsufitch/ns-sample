
CATEGORIES = [
    'PERSON',
    'PLACE',
    'ANIMAL',
    'COMPUTER',
    'OTHER',
    ]

class ThingStorage(object):
    def __init__(self):
        self.pairset = set()
        self.pairs = []
        self.counts = {c:0 for c in CATEGORIES}

    def record(self, category, subcategory):
        if category not in CATEGORIES:
            return

        pair = (category, subcategory)
        if pair not in self.pairset:
            self.counts[category] += 1
            self.pairset.add(pair)
            self.pairs.append(pair)

    def parse_file(self, fileobj):
        for line in fileobj:
            line = line.strip()
            if not line:
                continue
            category, subcategory = line.split(maxsplit=1)
            self.record(category, subcategory)

    def output_categories(self):
        print("CATEGORY    COUNT")
        for category in CATEGORIES:
            print("%s    %d" % (category, self.counts[category]))

    def output_pairs(self):
        for category, subcategory in self.pairs:
            print("%s    %s" % (category, subcategory))
