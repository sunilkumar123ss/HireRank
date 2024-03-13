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

    def test_aliases_match_canonical_requirement(self):
        result = evaluate(self.data)["profiles"][1]
        self.assertTrue(result["requirements"][2]["evidence_supplied"])
        self.assertEqual(canonical(" SpringBoot "), "Spring Boot")

    def test_missing_required_evidence_is_explicit(self):
        result = evaluate(self.data)["profiles"][1]
        self.assertEqual(result["missing_required_evidence"], ["FastAPI"])

    def test_evidence_is_preserved_and_not_verified(self):
        result = evaluate(self.data)["profiles"][0]["requirements"][0]
        self.assertEqual(result["evidence"][0], self.data["profiles"][0]["skills"][0]["evidence"])
        self.assertEqual(result["verification"], "unverified supplied text")
