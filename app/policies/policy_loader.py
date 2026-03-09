import yaml

def load_policy():
    with open("config/reward_policy.yaml") as f:
        return yaml.safe_load(f) # converts the YAML content into a Python dictionary

policy = load_policy() 