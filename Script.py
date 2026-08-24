def test_addition():
    a = 125
    b = 126
    expected_result = 251
    
    actual_result = a + b
    
    assert actual_result == expected_result
    print("Test passed: Addition is correct.")
    
if __name__ == "__main__":
    test_addition()