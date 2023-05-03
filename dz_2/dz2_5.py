def create_name_age_strings(names, ages):
    return [f"{name} - {age}" for name, age in zip(names, ages)]

def test_create_name_age_strings():
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    expected = ["Alice - 25", "Bob - 30", "Charlie - 35"]
    result = create_name_age_strings(names, ages)
    assert result == expected

    names = []
    ages = []
    expected = []
    result = create_name_age_strings(names, ages)
    assert result == expected
    print("All test_create_name_age_strings pass")

test_create_name_age_strings()