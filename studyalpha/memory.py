"""
Memory bank (local RAG) implemented with TF-IDF.
Stores textual records (quiz results, explanations, notes) and supports retrieval.
"""
import json
from typing import List, Dict, Any
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .utils import trace

class MemoryBank:
    def __init__(self):
        self.long_term: List[Dict[str, Any]] = []
        self.vectorizer: TfidfVectorizer | None = None
        self.tfidf_matrix = None

    def add(self, text: str, meta: Dict[str, Any] | None = None) -> int:
        idx = len(self.long_term)
        record = {"id": idx, "text": text, "meta": meta or {}}
        self.long_term.append(record)
        trace("memory.add", {"id": idx, "meta": meta})
        self._reindex()
        return idx

    def _reindex(self):
        corpus = [r["text"] for r in self.long_term]
        if corpus:
            self.vectorizer = TfidfVectorizer(stop_words="english").fit(corpus)
            self.tfidf_matrix = self.vectorizer.transform(corpus)
        else:
            self.vectorizer = None
            self.tfidf_matrix = None

    def query(self, q: str, top_k: int = 3) -> List[Dict[str, Any]]:
        if self.tfidf_matrix is None or self.vectorizer is None:
            return []
        q_vec = self.vectorizer.transform([q])
        scores = cosine_similarity(q_vec, self.tfidf_matrix)[0]
        idxs = np.argsort(scores)[::-1][:top_k]
        results = []
        for i in idxs:
            if scores[int(i)] > 0:
                results.append(self.long_term[int(i)])
        trace("memory.query", {"query": q, "results": [r["id"] for r in results]})
        return results

    def dump(self, path: str = "memory_dump.json"):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.long_term, f, indent=2)
        trace("memory.dump", {"path": path})
