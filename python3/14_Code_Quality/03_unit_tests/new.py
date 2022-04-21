import rdflib
g = rdflib.Graph()

# RDF - Resource Description Framework (RDF)

# g.parse("http://danbri.org/foaf.rdf#")

# knows_query = """
# SELECT DISTINCT ?aname ?bname
# WHERE {
#     ?a foaf:knows ?b .
#     ?a foaf:name ?aname .
#     ?b foaf:name ?bname .
# }"""

# qres = g.query(knows_query)
# for row in qres:
#     print(f"{row.aname} knows {row.bname}")


# g.parse("https://query.wikidata.org/sparql")
# print(len(g))

import requests

resp = requests.get('https://query.wikidata.org/sparql')
print(vars(resp))