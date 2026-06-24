"""rag — a naive RAG pipeline over 10-K SEC filings.

Modules
-------
config   : paths, model names, and tunable constants (chunk size, top_k, ...)
load     : read parquet filings and extract clean text
chunk    : split documents into overlapping passages
embed    : turn text into vector embeddings
store    : build and query the vector database
generate : build the prompt and call the LLM for the final answer

Indexing phase (run once):  load -> chunk -> embed -> store
Query phase (run per question):  embed(question) -> store.search -> generate
"""
