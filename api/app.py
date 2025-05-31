from flask import Flask, request, jsonify
from ai_agent.parser import parse_prompt
from ai_agent.generator import generate_network_yaml

app = Flask(__name__)

@app.route("/deploy", methods=["POST"])
def deploy():
    prompt = request.json.get("prompt", "")
    parsed = parse_prompt(prompt)
    yaml_output = generate_network_yaml(parsed)
    with open("network.yaml", "w") as f:
        f.write(yaml_output)
    return jsonify({"status": "success", "parsed": parsed})

if __name__ == "__main__":
    app.run(port=5000)
