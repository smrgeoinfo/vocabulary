"""Script to generate markdown from a SKOS vocabulary.
The generated markdown is intended for rendering with Quarto.

Original python by Dave Vieglais for iSamples project
from https://github.com/isamplesorg/isamplesorg.github.io
Supported by NSF funding: Collaborative Research: Frameworks: 
Internet of Samples: Toward an Interdisciplinary Cyberinfrastructure 
for Material Samples, Award Number:2004815; 

S.M. Richard 2023-02-27 Updated to show some other SKOS properties 
and change formating

This code reads a skos vocabulary file, serialized as turtle, 
from a URL and writes a markdown file to the stdout. 
The markdown uses some special syntax that is interpreted by 
Quarto for better html rendering

the conversion process fails if there are any non-base ASCII characters 
in the source files. 

license: Apache License 2.0

"""

import sys
import textwrap
import click
import rdflib
import datetime

import os
os.environ["PYTHONIOENCODING"] = "utf-8"

NS = {
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "obo": "http://purl.obolibrary.org/obo/",
    "dcterms": "http://purl.org/dc/terms/"
}

PFX = """
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
"""

INDENT = "  "

def skosT(term):
    return rdflib.URIRef(f"{NS['skos']}{term}")


def rdfT(term):
    return rdflib.URIRef(f"{NS['rdf']}{term}")


def rdfsT(term):
    return rdflib.URIRef(f"{NS['rdfs']}{term}")

def dctT(term):
    return rdflib.URIRef(f"{NS['dcterms']}{term}")


def listVocabularies(g):
    """List the vocabularies in the provided graph
    """
    q = PFX + """SELECT ?s
    WHERE {
        ?s rdf:type skos:ConceptScheme.
    }"""
    qres = g.query(q)
    res = []
    for r in qres:
        res.append(r[0])
    return res


def getVocabRoot(g, v):
    """Get top concept of the specific vocabulary
    """
    q = PFX + """SELECT ?s   WHERE { ?s skos:topConceptOf ?vocabulary . }"""
    qres = g.query(q, initBindings={'vocabulary': v})
    res = []
    for row in qres:
        res.append(row[0])
    return res


def getNarrower(g, v, r):
    q = rdflib.plugins.sparql.prepareQuery(PFX + """SELECT ?s
    WHERE {
        ?s skos:inScheme ?vocabulary .
        ?s skos:broader ?parent .
    }""")
    qres = g.query(q, initBindings={'vocabulary': v, 'parent': r})
    res = []
    for row in qres:
        res.append(row[0])
    return res


def getObjects(g, s, p):
    q = rdflib.plugins.sparql.prepareQuery(PFX + """SELECT ?o
    WHERE {
        ?subject ?predicate ?o .
    }""")
    qres = g.query(q, initBindings={'subject': s, 'predicate': p})
    res = []
    for row in qres:
        res.append(row[0])
    return res


def _labelToLink(label):
    if isinstance(label, list):
        label = label[0]
    label = label.split("/")[-1]
    label = label.lower().strip()
    label = label.replace(",", "")
    label = label.replace(" ", "-")
    return label


def termTree(g, v, r, depth=0):
    label = getObjects(g, r, skosT("prefLabel"))
#    print(label)
    llabel = _labelToLink(r)
    if not label:
        label = []
        label.insert(0, llabel)
    res = [f"{'    ' * depth}- [{label[0]}](#{llabel})"]
    for term in getNarrower(g, v, r):
        res += termTree(g, v, term, depth=depth + 1)
    return res


def termJsonTree(g, v, r, depth=0):
    label = getObjects(g, r, skosT("prefLabel"))[0]
    llabel = _labelToLink(r)
    obj = {
        "name": label,
        "target": llabel,
    }
    # res = [f"{'    '*depth}- [{label[0]}](#{llabel})"]
    children = []
    for term in getNarrower(g, v, r):
        children.append(termJsonTree(g, v, term, depth=depth + 1))
    obj["children"] = children
    return obj


def describeTerm(g, t, depth=0, level=1):
    res = []
    labels = getObjects(g, t, skosT('prefLabel'))
# anchor to link to this term
    _target = t.split("/")[-1]
    res.append("[]{" + f"#{_labelToLink(_target)}" + "}")
    res.append("")
# heading for this term
    hl = f"{'#' * (depth + 1)} "
    if len(labels) < 1:
        res.append(f"{hl} `{t}`")
    else:
        res.append(f"{hl} {labels[0].strip()}")
        for label in labels[1:]:
            res.append(f"* `{label}`")
        res.append("")

    broader = getObjects(g, t, skosT('broader'))
    if len(broader) > 0:
        res.append("")
        res.append(f"- Child of:")
        for b in broader:
            bt = b.split('/')[-1]
            res.append(f" [`{bt}`](#{bt})")
    res.append("")
    # The textual description will be present in rdfs:comment or
    # skos:definition. 
    comments = []
    for comment in getObjects(g, t, rdfsT('comment')):
        comments.append(f"- {comment}")
    for comment in getObjects(g, t, skosT('definition')):
        comments.append(f"- {comment}")
    for comment in comments:
        lines = textwrap.wrap(
            comment,
            width=70
        )
        res += lines
    seealsos = getObjects(g, t, rdfsT('seeAlso'))
    if len(seealsos) > 0:
        res.append("")
        res.append(f"- See Also:")
        for seealso in seealsos:
            res.append(f"* [{seealso.n3(g.namespace_manager)}]({seealso})")
    altlabels = []
    for altlabel in getObjects(g, t, skosT('altLabel')):
        altlabels.append(altlabel)
    if len(altlabels) > 0:
        delimiter = ""
        if len(altlabels) > 1:
            delimiter = ", "
        res.append("")
        res.append(f"- **Alternate labels:**")
        for altlabel in altlabels:
            res.append(f"{altlabel}{delimiter}")
        res.append("")

    sources = []
    for source in getObjects(g, t, dctT('source')):
        sources.append(source)
    if len(sources) > 0:
        delimiter = ""
        if len(sources) > 1:
            delimiter = ", "
        res.append("")
        res.append(f"- **Source:**")
        for source in sources:
            res.append(f"{source}{delimiter}")
        res.append("")

    res.append(f"- Concept URI token: {t.split('/')[-1]}")
    res.append("")

    return res


def describeNarrowerTerms(g, v, r, depth=0, level=[]):
    res = []
    terms = getNarrower(g, v, r)
    for term in terms:
        res += describeTerm(g, term, depth=depth)
        res.append("")
        res += describeNarrowerTerms(g, v, term, depth=depth + 1)
    return res


def describeVocabulary(G, V):
    res = []
    level = [1, ]
    title = getObjects(G, V, skosT("prefLabel"))[0]
    # this is the header for Quarto...
    res.append("---")
    res.append("comment: |  WARNING: This file is generated. Any edits will be lost!")
    res.append(f"title: \"{title.strip()}\"")
    res.append("format:")
    res.append("  html:")
    res.append("    ascii: true")
    res.append("    toc: true")
    res.append("    toc-depth: 4")
    res.append("    number-sections: true")
    res.append("    anchor-sections: false")
    res.append("    number-depth: 8")
    res.append("from: markdown+hard_line_breaks")
    res.append("execute:")
    res.append("  echo: false")
#    res.append("categories: [\"vocabulary\"]")
    res.append("---")
    # end quarto header
    res.append("")

    scheme = getObjects(G, V, skosT("prefLabel"))[0]
    lscheme = scheme.replace(" ","")
    res.append("[]{" + f"#{lscheme}" + "}")
    res.append("")
    res.append(f"# **Concept scheme:** {scheme}")
    res.append("")

    modified = getObjects(G, V, dctT("modified"))[0]
    res.append(f"Vocabulary last modified:  {modified}")
    res.append("")

    res.append("subtitle: ")
    for comment in getObjects(G, V, skosT("definition")) + getObjects(G, V, rdfsT("comment")):
        res.append(f"  {comment.strip()}")
    res.append("")
    res.append("Namespace: ")
    res.append(f"[`{V}`]({V})")
    res.append("")
    res.append("**History**")
    res.append("")
    for history in getObjects(G, V, skosT("historyNote")):
        res.append(f"* {history}")
    res.append("")

    depth = 1
    roots = getVocabRoot(G, V)
#
    for root in roots:
        res += termTree(G, V, root, depth=0)
        res.append("")
    # res.append("```{ojs}")
    # res.append("import {Tree} from '@d3/tree'")
    # res.append(TREE_CHART_SCRIPT)
    # res.append(f"vocab_terms=JSON.parse({json.dumps(json.dumps(termJsonTree(G, V, roots[0], depth=0)))});")
    # res.append(TREE_CHART_BLOCK)
    # res.append("```")
    res.append("**Concepts**")
    res.append("")
    for aroot in roots:
        res += describeTerm(G, aroot, depth=depth, level=level)
        res.append("")
        res += describeNarrowerTerms(G, V, aroot, depth=depth + 1, level=level)
        res.append("")
    return res

def conceptschemelist(G):
    vocabs = listVocabularies(G)
    res = []
    res.append("")
    res.append(f"# Concept Schemes in this file")
    res.append("")
    for vocab in vocabs:
        label = getObjects(G, vocab, skosT("prefLabel"))
        llabel = label[0].replace(" ", "")
        res.append(f"[{label[0]}](#{llabel})")
        res.append("")

    res.append("")
    res.append(
        f"This file generated at: \"{datetime.datetime.now().replace(tzinfo=datetime.timezone.utc).isoformat()}\"")

    return res

@click.command()
@click.argument("ttl")


def main(ttl):
    # ttl is argument, remove for debugging
    """Generate Pandoc markdown from a SKOS vocabulary in Turtle.

    TTL may be a local file or URL.
    Output to STDOUT.
    """
    #for debugging
    #ttl = "https://raw.githubusercontent.com/smrgeoinfo/vocabulary/main/geochemistry/AnalyticalTechniqueMerg2.ttl"
    #  ttl = "C:\\Workspace\\GithubC\\iSamples\\vocabularies\\src\\extensions\\specimenTypeExtension.ttl"
    vgraph = rdflib.ConjunctiveGraph()
    vgraph.parse(ttl, format="text/turtle")
    for k, v in NS.items():
        vgraph.bind(k, v)
    vocabs = listVocabularies(vgraph)
    res = []

    res.append(conceptschemelist(vgraph))

    for vocab in vocabs:
        res.append(describeVocabulary(vgraph, vocab))

    for doc in res:
        for line in doc:
 #           print(line.encode('utf-8'))
            print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
