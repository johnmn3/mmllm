"""Aesop capstone — physically-consistent procedural story generator.

Generates English narratives with embedded Clojure expressions and tool-call
answers, where every record's math is verified by actually evaluating the
expression tree. Built around 10 Aesop fables decomposed into chapters
parameterized over a typed entity ontology (items, containers, characters,
locations) with cross-template constraints (e.g., "this item must fit in
this container", "these two characters must have different names").

Modules:
  ontology  — entity types + catalogs + fit predicates
  expr      — small arithmetic AST with eval + Clojure emitter (single
              source of truth for the math)
  template  — variable resolver with typed constraints
  fables    — the 10 fable definitions (chapter trees)
  generate  — corpus generator (template → record), math verifier,
              train/val/test splitter
"""
