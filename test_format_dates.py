import pytest
from datetime import datetime
from format_dates import lambda_handler

# Define test cases
test_cases = [
    {
        "input": {
            "State": {
                "EnteredTime": "2023-10-15T12:34:56.789Z"
            }
        },
        "expected": {
            "today": "2023-10-15",
            "yesterday": "2023-10-14"
        }
    },
    {
        "input": {
            "State": {
                "EnteredTime": "2023-01-01T00:00:00.000Z"
            }
        },
        "expected": {
            "today": "2023-01-01",
            "yesterday": "2022-12-31"
        }
    },
    # Add more test cases as needed
]

@pytest.mark.parametrize("test_case", test_cases)
def test_lambda_handler(test_case):
    result = lambda_handler(test_case["input"], None)
    assert result == test_case["expected"]
