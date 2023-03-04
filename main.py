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


