import yaml

def generate_network_yaml(parsed_config):
    config = {
        "version": "1.0",
        "organizations": parsed_config["orgs"],
        "channel": parsed_config["channel"],
        "identity": parsed_config["identity"],
        "deployment": parsed_config["deployment"],
        "chaincode": parsed_config["chaincode"]
    }
    return yaml.dump(config)
