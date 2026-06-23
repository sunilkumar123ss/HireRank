# HireRank

**Explain technical evidence coverage without making a hiring decision.**

HireRank compares a job's explicit technical requirements with structured, supplied skill evidence. It preserves each evidence statement, shows missing evidence, and explains the numerator and denominator of a weighted coverage percentage. Profiles remain in input order; the tool does not rank people or issue accept/reject recommendations.

## Run

Python 3.9+ · standard library only.

```sh
python3 main.py
python3 main.py --input example.json
python3 main.py --help
python3 -m unittest discover -s . -p 'test_main.py' -v
```

Default demo and help work from any working directory. The default synthetic fixture is located next to the script. Explicit input paths follow the caller's working directory.

## Transparent scoring

Requirements contain `skill`, an integer `weight` from 1–10, and a `required` flag. Profile skill entries contain `skill` and non-empty `evidence`. A finite technical-skill catalog normalizes documented aliases such as `postgres` → `PostgreSQL`; unknown features are rejected. No age, gender, nationality, ethnicity, disability, location or other personal attribute is a scoring feature.

Coverage is `100 × matched requirement weight / total requirement weight`. Repeating skill evidence cannot increase it. Missing required evidence is listed separately. The fixture's first profile supplies evidence for Python and FastAPI, covering 5 of 6 weighted points (**83.33%**); the remaining point belongs to PostgreSQL.

Every supplied claim is labeled **unverified supplied text**. Missing evidence does not establish missing ability. Weights express the caller's requirements and can distort comparisons; the percentage measures checklist coverage, not job performance, competence or candidate quality. A person must verify evidence and assess context.

## Tests and scope

Nine tests cover weights, aliases, missing requirements, evidence fidelity, input ordering, duplicate requirements, blank evidence, unsupported features and duplicate evidence. All profiles and evidence in the fixture are synthetic.

This is a **Python reference core**. Java, Spring Boot, REST pagination, resume-file parsing, sentence-transformer embeddings and the Hugging Face Inference API are not implemented. It does not send applications or make employment decisions.

## Scope

Batch throughput and end-to-end latency have not been benchmarked.

## Repository checks

```sh
python3 verify.py
```

This runs the isolated test suite, synthetic example, and CLI help. The included GitHub Actions workflow repeats these checks when the repository is published. No hosted CI result is claimed by the local verification report.
