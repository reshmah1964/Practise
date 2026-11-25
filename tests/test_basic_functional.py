import pytest

from basic_functional_progras import (
    TIMED_TEST_RUNS,
    calculate_pass_percentage,
    find_fastest_test,
    find_slowest_test,
    group_test_results,
)


def test_find_slowest_test():
    assert find_slowest_test(TIMED_TEST_RUNS)["name"] == "checkout"


def test_find_fastest_test():
    assert find_fastest_test(TIMED_TEST_RUNS)["name"] == "profile"


@pytest.mark.parametrize("finder", [find_slowest_test, find_fastest_test])
def test_finders_return_none_for_empty_list(finder):
    assert finder([]) is None


def test_group_test_results_buckets_by_status():
    runs = [
        {"name": "a", "status": "PASS"},
        {"name": "b", "status": "FAIL"},
        {"name": "c", "status": "SKIP"},
    ]
    assert group_test_results(runs) == {
        "PASS": ["a"],
        "FAIL": ["b"],
        "SKIP": ["c"],
        "INVALID": [],
    }


# TODO(you): add tests for the edge cases group_test_results is meant to handle:
#   - a status with extra spaces and lowercase letters, like " pass "
#   - an unknown status, like "BROKEN"
#   - an empty list


@pytest.mark.parametrize(
    "total, passed, expected",
    [
        (5, 3, 60.0),
        (4, 4, 100.0),
        (4, 0, 0.0),
        (0, 0, None),   # no tests
        (3, 5, None),   # more passed than total
        (5, -1, None),  # negative count
    ],
)
def test_calculate_pass_percentage(total, passed, expected):
    assert calculate_pass_percentage(total, passed) == expected
