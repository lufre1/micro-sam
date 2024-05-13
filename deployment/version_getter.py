import runpy
import ruamel.yaml
import os

yaml = ruamel.yaml.YAML()
yaml.preserve_quotes = True

# Construct the filename based on OS name
construct_file = f"construct_{current_os}.yaml"

# Load YAML using ruamel.yaml
yaml = ruamel.yaml.YAML()
yaml.preserve_quotes = True

with open(construct_file, "r") as stream:
    ctor_conf = yaml.load(stream)

ctor_conf["version"] = runpy.run_path(os.path.join("..", "micro_sam", "__version__.py"))["__version__"]

with open(ctor_fname, "w") as outfile:
    yaml.dump(ctor_conf, outfile)
