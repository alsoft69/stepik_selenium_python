def test_substring(full_string, substring):
    result = substring in full_string
    assert result, f"expected '{substring}' to be substring of '{full_string}'"

x1 = input()
x2 = input()
test_substring(x1, x2)

