import copy
import json
from pathlib import Path
import unittest
from main import canonical, evaluate, explain


class EvidenceTests(unittest.TestCase):
    def setUp(self): self.data = json.loads(Path(__file__).with_name("example.json").read_text())

    def test_weighted_coverage_explains_numerator(self):
        result = evaluate(self.data)["profiles"][0]
        self.assertEqual(result["matched_weight"], 5)
        self.assertEqual(result["total_weight"], 6)
        self.assertEqual(result["weighted_coverage_percent"], 83.33)
