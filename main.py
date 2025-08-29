import json
from graphviz import Digraph

def json_to_flowchart(json_path, output_path="flowchart"):
    with open(json_path, 'r') as f:
        data = json.load(f)

    dot = Digraph()

    steps = data.get("steps", {})
    for step, transitions in steps.items():
        for key, value in transitions.items():
            if key == "next":
                dot.edge(step, value)
            elif key in ["yes", "no"]:
                dot.edge(step, value, label=key)

    dot.render(output_path, format='png', cleanup=True)
    print(f"Flowchart saved to {output_path}.png")


json_to_flowchart("data.json")
