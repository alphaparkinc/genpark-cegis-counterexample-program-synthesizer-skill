from client import CEGISSynthesizer

synthesizer = CEGISSynthesizer()
examples = [(1, 3), (2, 5), (3, 7)]
coeffs, expr = synthesizer.synthesize(examples)
print(f"Synthesized program: {expr} with coefficients: {coeffs}")
