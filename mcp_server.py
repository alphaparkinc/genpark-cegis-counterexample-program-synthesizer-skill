import sys
import json
from client import CEGISSynthesizer

synthesizer = CEGISSynthesizer()

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "cegis_synthesize",
                        "description": "Synthesize affine formula f(x) = a*x + b consistent with input-output examples",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "examples": {
                                    "type": "array",
                                    "items": {"type": "array", "items": {"type": "number"}}
                                }
                            },
                            "required": ["examples"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "cegis_synthesize":
            exs = [tuple(p) for p in args["examples"]]
            coeffs, formula = synthesizer.synthesize(exs)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps({"formula": formula, "coefficients": coeffs})}]}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if line.strip():
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
