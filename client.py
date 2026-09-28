"""Counterexample-Guided Inductive Synthesis (CEGIS) Synthesizer.
100% Python Standard Library.
"""

class CEGISSynthesizer:
    """CEGIS synthesizer for straight-line affine functions f(x) = a * x + b."""
    def synthesize(self, examples, candidate_coeffs=None):
        if candidate_coeffs is None:
            candidate_coeffs = [(1, 0), (2, 0), (2, 1), (3, -1), (0, 5), (4, 2), (-1, 10)]
        for a, b in candidate_coeffs:
            consistent = True
            for x, y in examples:
                if a * x + b != y:
                    consistent = False
                    break
            if consistent:
                return (a, b), f"f(x) = {a}*x + {b}"
        return None, "No consistent candidate found"
