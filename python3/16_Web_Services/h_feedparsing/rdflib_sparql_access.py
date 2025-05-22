import rdflib
from security import safe_requests

g = rdflib.Graph()

resp = safe_requests.get("https://query.wikidata.org/sparql", timeout=60)
print(vars(resp))
