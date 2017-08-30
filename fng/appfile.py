import json
import jsonschema
import yaml
import pkg_resources

from pathlib import Path
from .exception import AppfileNotFound


def load_schema(name):
    schema = pkg_resources.resource_string(__name__, "/".join(("jsonschema", name)))
    return json.loads(schema.decode("UTF-8"))


def load_appfile(validate=True):
    allowed_names = ["Appfile.yaml", "Appfile.yml", "Appfile"]
    allowed_names = allowed_names + [x.lower() for x in allowed_names]

    for name in allowed_names:
        try:
            with (Path(".") / name).open(mode="r") as f:
                raw = yaml.load(f)
                if validate:
                    jsonschema.validate(raw, load_schema("appfile.json"))

                return raw
        except FileNotFoundError:
            pass

    raise AppfileNotFound("Application config (Appfile.yaml) was not found")
