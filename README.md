# CEGIS Program Synthesizer Skill

High-efficiency, zero-dependency Python implementation of **Counterexample-Guided Inductive Synthesis (CEGIS)** for deductive program generation.

## Features
- **Specification Satisfiability**: Iteratively selects candidate programs and validates against accumulated counterexamples.
- **Deductive Synthesis Search**: Systematically prunes inconsistent program hypothesis classes.
- **Zero External Dependencies**: Pure Python standard library.
- **Native MCP Protocol**: JSON-RPC 2.0 stdio server compatible with Claude Desktop, Cursor, and Windsurf.

## Architecture
```mermaid
graph TD
    Spec["Input/Output Specifications"] --> Synthesizer["Synthesizer (Candidate Gen)"]
    Synthesizer --> Candidate["Candidate: f(x) = a*x + b"]
    Candidate --> Verifier["Verifier / Test Oracle"]
    Verifier -- Counterexample Found --> Synthesizer
    Verifier -- All Tests Pass --> Accepted["Synthesized Valid Program"]
```
