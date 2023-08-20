#!/usr/bin/env python3
"""Explain coverage of explicit technical requirements using supplied skill evidence."""
import argparse
import json
from pathlib import Path


CATALOG = {
    "python": "Python", "java": "Java", "sql": "SQL", "fastapi": "FastAPI",
    "spring boot": "Spring Boot", "springboot": "Spring Boot", "docker": "Docker",
    "postgresql": "PostgreSQL", "postgres": "PostgreSQL", "mysql": "MySQL",
    "redis": "Redis", "git": "Git", "langchain": "LangChain", "langgraph": "LangGraph",
    "rag": "RAG", "retrieval augmented generation": "RAG", "junit": "JUnit",
    "pytest": "pytest", "kubernetes": "Kubernetes", "javascript": "JavaScript",
    "typescript": "TypeScript", "aws": "AWS", "linux": "Linux", "rest api": "REST APIs",
    "rest apis": "REST APIs", "mcp": "MCP", "spring batch": "Spring Batch",
}


def canonical(skill):
    if not isinstance(skill, str): raise ValueError("skill must be text")
    key = " ".join(skill.casefold().strip().split())
    if key not in CATALOG:
        raise ValueError("unsupported technical skill: " + skill)
    return CATALOG[key]


def explain(requirements, profile):
    if not isinstance(requirements, list) or not requirements:
        raise ValueError("at least one technical requirement is needed")
    if not isinstance(profile, dict) or not isinstance(profile.get("id"), str) or not profile["id"]:
        raise ValueError("profile requires an id")
    skills = profile.get("skills")
    if not isinstance(skills, list): raise ValueError("skills must be a list")
    evidence = {}
    for item in skills:
        if not isinstance(item, dict): raise ValueError("skill evidence must be an object")
        name = canonical(item.get("skill"))
        quote = item.get("evidence")
        if not isinstance(quote, str) or not quote.strip(): raise ValueError("every supplied skill needs evidence text")
        evidence.setdefault(name, [])
        if quote not in evidence[name]: evidence[name].append(quote)
    rows, seen, total, matched = [], set(), 0, 0
    for requirement in requirements:
        if not isinstance(requirement, dict): raise ValueError("requirement must be an object")
        name = canonical(requirement.get("skill"))
        if name in seen: raise ValueError("duplicate canonical requirement")
        seen.add(name)
        weight, required = requirement.get("weight", 1), requirement.get("required", False)
        if type(weight) is not int or not 1 <= weight <= 10: raise ValueError("weight must be integer 1..10")
        if type(required) is not bool: raise ValueError("required must be boolean")
        supplied = name in evidence
        total += weight
        if supplied: matched += weight
        rows.append({"skill": name, "weight": weight, "required": required, "evidence_supplied": supplied,
                     "evidence": evidence.get(name, []), "verification": "unverified supplied text" if supplied else "no evidence supplied"})
    return {"profile_id": profile["id"], "weighted_coverage_percent": round(100 * matched / total, 2),
            "matched_weight": matched, "total_weight": total, "requirements": rows,
            "missing_required_evidence": [row["skill"] for row in rows if row["required"] and not row["evidence_supplied"]],
            "interpretation": "Coverage of supplied technical evidence only; no hiring decision or candidate ranking."}


def evaluate(request):
    if not isinstance(request, dict) or not isinstance(request.get("profiles"), list):
        raise ValueError("input needs a profiles list")
    profiles = request["profiles"]
    ids = [profile.get("id") if isinstance(profile, dict) else None for profile in profiles]
    if any(not isinstance(key, str) for key in ids) or len(set(ids)) != len(ids):
        raise ValueError("profile ids must be unique strings")
    return {"profiles": [explain(request.get("requirements"), profile) for profile in profiles],
            "order": "input order preserved", "uses_personal_attributes": False}
