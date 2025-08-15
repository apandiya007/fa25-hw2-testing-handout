> [!CAUTION]
> This repository is for viewing only. Do not work on the assignment using this repository -- the actual course assignments will be provided to you via Pawtograder.

# Homework 2: Testing 311 Service Request Processing

## Learning Outcomes

- Debug existing code
- Write tests to catch bugs in unseen code
- Practice adhering to the level of visibility set in existing code for attributes and properties
- Use Generic type annotations
- Consider the privacy of people in a dataset

## Overview

Homework 2 is to write tests for two of the classes that you will implement in Homework 3.
We have (hidden) implementations of the classes in the autograder for Homework 2, but there are bugs in them.
Your task is to write tests that catch those bugs.

Homework 3 will involve analyzing a dataset of 311 service request data to explore how municipal services are distributed across different neighborhoods and demographics. 311 systems allow residents to report non-emergency issues like potholes, broken streetlights, noise complaints, and other quality-of-life concerns.
You will analyze one of these two datasets:
- Oakland/San Francisco: https://data.sfgov.org/City-Infrastructure/311-Cases/vw6y-z8j6/data_preview
- Boston: https://data.boston.gov/dataset/311-service-requests

You will write tests for two classes: `DataLoader` and `data_loader.py`.

These classes are designed to analyze large datasets. It is impractical for tests to also involve large datasets, so there are sample datasets in `example_CSVs`. You should use these smaller datasets to implement your tests.

## Your Tasks

### Part 1: Look at the classes

You will write tests for two classes: `DataLoader` and `data_loader.py`. The stub implementations for these classes are provided in `data_loader.py` and `sorting.py`, respectively.
Look at these two classes and take note of cases that would be good to test.

Remember: when testing, we want to consider:
- the "happy path" with valid input
- any invalid inputs
- any edge cases (almost invalid but still valid)

### Part 2: Test DataLoader

There are some test method stubs provided in `test_data_loader.py`. Implement all of the required tests.
Remember: you are expected to use the sample datasets in `example_CSVs`.

### Part 3: Test CaseSorter

Unlike `TestDataLoader`, `TestCaseSorter` does not contain test method stubs. Your task is to come up with the test cases.

The autograder contains a few implementations of `CaseSorter`, each with a different bug. It will run your tests on our buggy implementations, and calculate how many of the bugs are caught by your tests.

### Part 4: Summary.md

Answer all of the questions in `Summary.md`.

## Running Tests
To run your tests, you can use the provided `test_runner.py`. Run `python3 test_runner.py` to run all tests in the `tests/` directory. 

If you try to run the test files directly, you will face an import error due to the way the assignment is structured. DO NOT try to fix this import error, and leave the imports as they are provided in the handout. Othwerwise, the autograder may not be able to run your tests properly, since it uses test_runner.py, and expects tests to execute properly that way. 

While you are completing the test files, you may want to run individual test files at a time, instead of running them all at once. To do this, you can run `test_runner.py` with the `-t` option in your terminal to only run tests in the files you specify. Note: the test file names you provide must exist in the `tests/` directory, or they won't run. 

Example command to only run tests in test_sorting.py:
```python3 test_runner.py -t test_sorting.py```

You can also run multiple test files by listing the file names after the -t option. 
Example command to run multiple test files: 
```python3 test_runner.py -t test_sorting.py test_data_loader.py```

If you just want to run all tests in the tests/ directory, you can run `python3 test_runner.py` omitting the `-t` flag at the end. This will run all test files with the pattern `test_*.py` or `impl_*.py` inside of the tests/ directory. Make sure all your test file names start with either `test_` or `impl_`, or else they will not run.

## Generating Coverage reports

Run the following command in your terminal to generate coverage reports:

```./generate_coverage_reports```

A link to the a html page containing the coverage reports will be produced in the output of the command. You can click on it to view detailed coverage reports. 

These reports indicate how much of your code is being executed by your tests. This is a purely syntactic check, and having full coverage does not necessarily mean your tests are sufficient, but it's a good starting point. You should aim to have full coverage (ie. every line of your code gets executed by your tests)


## Grading Rubric
- Implementing the test stubs in `TestDataLoader` (30%)
- Catching our hidden bugs using `TestCaseSorter` (35%)
- Summary.md (35%)

Good luck!
