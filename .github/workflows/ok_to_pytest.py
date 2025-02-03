import subprocess
import sys

def run_ok_test(test_name):
    """Run ok --score and check the score for a specific test"""
    result = subprocess.run([sys.executable, 'ok', '--score'], capture_output=True, text=True)
    
    # Find score for specific test
    for line in result.stdout.split('\n'):
        if test_name in line and ': ' in line:
            score_part = line.split(': ')[1]
            actual_score, total_score = map(float, score_part.split('/'))
            assert actual_score == total_score, f"{test_name} received {actual_score}/{total_score} points instead of full credit"
            return
    
    # If we didn't find the test
    assert False, f"Could not find score for {test_name}"

def test_broken_factorial_0():
    run_ok_test("test_ses03_solution_broken_factorial_0")

def test_broken_factorial_1():
    run_ok_test("test_ses03_solution_broken_factorial_1")

def test_broken_factorial_2():
    run_ok_test("test_ses03_solution_broken_factorial_2")

def test_broken_factorial_3():
    run_ok_test("test_ses03_solution_broken_factorial_3")

def test_item_lengths_0():
    run_ok_test("test_ses03_solution_item_lengths_0")

def test_item_lengths_1():
    run_ok_test("test_ses03_solution_item_lengths_1")

def test_item_lengths_2():
    run_ok_test("test_ses03_solution_item_lengths_2")

def test_longest_item_0():
    run_ok_test("test_ses03_solution_longest_item_0")

def test_longest_item_1():
    run_ok_test("test_ses03_solution_longest_item_1")

def test_longest_item_2():
    run_ok_test("test_ses03_solution_longest_item_2")
