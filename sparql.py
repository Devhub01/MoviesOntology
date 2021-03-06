
import requests
import json

class Sparql:

    endpoint = 'http://localhost:3030/bdsproject/'

    prefixes = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX mov: <http://www.semanticweb.org/daniel/ontologies/moviesAndSeries#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>"""


    def select(self, triple):
        response = requests.post(self.endpoint + 'query', data = { 'query' : self.prefixes + triple })
        return response.json()