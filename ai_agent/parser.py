def parse_prompt(prompt):
    """
    Parses a natural language prompt and returns a dictionary
    with extracted deployment parameters.
    """
    result = {
        "orgs": [],
        "channel": "mychannel",
        "chaincode": {
            "name": "basiccc",
            "version": "1.0",
            "language": "golang"
        },
        "identity": "fabric-ca",
        "deployment": "docker"
    }

    prompt_lower = prompt.lower()

    # Org names
    for keyword in ["sbi", "icici", "alpha", "beta"]:
        if keyword in prompt_lower:
            result["orgs"].append(keyword.upper())

    # Channel
    if "channel" in prompt_lower:
        tokens = prompt_lower.split()
        for i, token in enumerate(tokens):
            if "channel" in token and i > 0:
                result["channel"] = tokens[i - 1]

    # Chaincode name
    for word in prompt_lower.split():
        if "cc" in word:
            result["chaincode"]["name"] = word

    # Language
    if "golang" in prompt_lower:
        result["chaincode"]["language"] = "golang"
    elif "node" in prompt_lower or "nodejs" in prompt_lower:
        result["chaincode"]["language"] = "node"

    # Identity management
    if "cryptogen" in prompt_lower:
        result["identity"] = "cryptogen"

    # Deployment
    if "kubernetes" in prompt_lower or "k8s" in prompt_lower:
        result["deployment"] = "kubernetes"

    return result
