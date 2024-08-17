import yaml
import os

from fastapi import FastAPI

app = FastAPI(debug=True, openapi_url='/api/openapi.json', docs_url='/api/docs')

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir_path, '../oas.yaml')

oas_doc = yaml.safe_load(open(filename, 'r'))

app.openapi = lambda: oas_doc
