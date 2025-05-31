import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ai_agent.parser import parse_prompt
from ai_agent.generator import generate_network_yaml

def main():
    prompt = input("Enter your Fabric deployment prompt:\n")
    parsed = parse_prompt(prompt)
    yaml_output = generate_network_yaml(parsed)
    with open("network.yaml", "w") as f:
        f.write(yaml_output)
    print("✅ Generated network.yaml based on your prompt.")

if __name__ == "__main__":
    main()
