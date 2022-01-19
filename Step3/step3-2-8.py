def test_input_text(expected_result, actual_result):
    result = expected_result == actual_result
    assert result, f'expected {expected_result}, got {actual_result}'

x1 = int(input())
x2 = int(input())

test_input_text(x1, x2)

