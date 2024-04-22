# FILEPATH: /Users/ahle/repos/dspy/tests/evaluate/test_metrics.py

import dspy
from dspy.evaluate.metrics import answer_exact_match
from dspy.primitives.prediction import Prediction


def test_answer_exact_match_string():
    example = dspy.Example(
        question="What is 1+1?",
        answer="2",
    ).with_inputs("question")

    pred = Prediction.from_completions([{"answer": "2"}])
    assert answer_exact_match(example, pred)


def test_answer_exact_match_list():
    example = dspy.Example(
        question="What is 1+1?",
        answer=["2", "two"],
    ).with_inputs("question")
    pred = Prediction.from_completions([{"answer": "2"}])
    assert answer_exact_match(example, pred)


def test_answer_exact_match_no_match():
    example = dspy.Example(
        question="What is 1+1?",
        answer="2",
    ).with_inputs("question")

    pred = Prediction.from_completions([{"answer": "3"}])
    assert not answer_exact_match(example, pred)
