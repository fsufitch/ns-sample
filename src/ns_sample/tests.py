def setup_storage():
    from ns_sample.storage import ThingStorage
    return ThingStorage()

def test_defaults():
    storage = setup_storage()
    assert storage.counts == {
        'PERSON': 0,
        'PLACE': 0,
        'ANIMAL': 0,
        'COMPUTER': 0,
        'OTHER': 0,
        }
    assert not storage.pairs
    assert not storage.pairset

def test_parsing():
    parsed_data = []
    def mock_record(category, subcategory):
        parsed_data.append( (category, subcategory) )

    storage = setup_storage()
    storage.record = mock_record
    
    from io import StringIO
    data = StringIO("Bob Smith\nFoo Bar\nFoobar McWumpus The 2nd\n")
    
    storage.parse_file(data)
    assert parsed_data == [
        ('Bob', 'Smith'),
        ('Foo', 'Bar'),
        ('Foobar', 'McWumpus The 2nd'),
        ]

def test_recording():
    parsed_data = [
        ("PERSON", "John Smith"),
        ("PERSON", "Filip Sufitchi"),
        ("COMPUTER", "Dell"),
        ("ANIMAL", "Dog"),
        ("PERSON", "Filip Sufitchi"),
        ]
    
    storage = setup_storage()
    for category, subcategory in parsed_data:
        oldcount = storage.counts[category]
        already_in_set = (category, subcategory) in storage.pairset
        storage.record(category, subcategory)
        assert (category, subcategory) in storage.pairset
        if not already_in_set:
            assert storage.counts[category] == oldcount+1
            assert (category, subcategory) == storage.pairs[-1]

    assert storage.pairset==set(parsed_data)
    assert storage.pairs==[
        ("PERSON", "John Smith"),
        ("PERSON", "Filip Sufitchi"),
        ("COMPUTER", "Dell"),
        ("ANIMAL", "Dog"),
        ]
    print(storage.counts)
    assert storage.counts=={
        "PERSON": 2,
        "COMPUTER": 1,
        "ANIMAL": 1,
        "PLACE": 0,
        "OTHER": 0,
        }

def test_ignore_bad_category():
    storage = setup_storage()
    storage.record("BAD CATEGORY", "Some subcategory")
    assert not storage.pairs
    assert not storage.pairset
    assert not any(storage.counts.values())

