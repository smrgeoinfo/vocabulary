# What is here:

## Geochemistry folder
Vocabularies for for analytical techniques in geochemistry (work started 2/2023).  The directory contains SKOS vocabulary drafts, serialized using turtle (ttl). HTML versions are generated on the pages branch in this repo using the scripts in the scripts folder on the pages branch.  The html is accessible on the github.io pages for the repo, links included in vocabulary descriptions.

### AnalyticalTechniqueMerg2.ttl
SKOS vocabualary, serialized using Turtle.  Merged analytical techniques from GeoX, GeoRock, PetDb, OSIRIS-REX.  General technique concepts added to generate hierarchy by SMR. This is a work in progress, please add comments and suggestions in the GitHub issue tracker. 
[HTML view of Analytical Techniques Merged vocabulary draft]( https://smrgeoinfo.github.io/vocabulary/geochemistry/html/AnalyticalTechniqueMerg2.html)

### GeoXAnalyticalTechnique.ttl
SKOS vocabualary, serialized using Turtle. Based on Geo-X spreadsheet from Manja Luzi (GFZ Potsdam), with some general categories added to fill out the hierarchy. This is input to AnalyticalTechniqueMerg2.ttl.
[HTML view of GeoX Analytical Techniques vocabulary draft]( https://smrgeoinfo.github.io/vocabulary/geochemistry/html/GeoXAnalyticalTechnique.html)

## pages branch 

### [scripts](https://github.com/smrgeoinfo/vocabulary/tree/pages/scripts)
Shell script and python code from Dave Vieglais. Generates Markdown view of the SKOS, and then renders that to html using quarto. To run you'll need a python environment with click and rdflib loaded. Instructions at https://github.com/isamplesorg/isamplesorg.github.io/blob/main/README.md are helpful. The html gets put in the html folder in the appropriate vocabulary subfolder. The scripts access the vocabulary using http from the github repository.  To run check out the repo, create a branch for your work, load your python environment, run the .sh script (in windows you might need to get WSL (Windows Subsystem for Linux) running, (https://linuxhint.com/run-sh-file-windows/ might be helpful). Then push changes to your branch (or fork if permissions don't allow). If it looks good, put in a pull request to merge into master.


# lithology

## [GSQ lithology vocabulary](https://github.com/smrgeoinfo/vocabulary/blob/main/lithology/GSQlithology.ttl)
[Hosted in GitHub](https://github.com/geological-survey-of-queensland/vocabularies/blob/master/vocabularies-gsq/lithology.ttl)
Derived from the IUGS classification scheme, CGI SImple Lithology, British Geological Survey, Meteoritical Society, accumulated GSQ information, and consultation with the Queensland Resources Industry, with cross referencing to mindat.org. skos match relations link to CGI Simple Lithology classes.
SKOS, rock types are skos:Concept instances. skos:broader relations denote hierarchy. 2968 skos:Concept instances (assume each is a lithology class)

## BGS Rock Names (earth-material-class.nt)
[Hosted in GitHub](https://github.com/BritishGeologicalSurvey/vocabularies/blob/main/vocabularies/earth-material-class.nt). No file-level metadata, not an owl:ontology.
Documentation at Earth Material Class (Rock Classification Scheme) web site:
The BGS Earth Material Class scheme is a linked data representation of the BGS Rock Classification Scheme (RCS), which is a corporate standard setting out a practical, logical and robust system for classifying and naming geological materials as they appear at the scale of a single exposure, hand specimen, or thin section. Classification helps to place materials in a wider geological context, and allows unambiguous and informative formal names to be assigned.  The RCS provides a comprehensive system for classifying and naming geological materials to act as a corporate standard in support of our digital geological maps, data dictionaries, and numerous other geological applications. [Web page](https://data.bgs.ac.uk/doc/EarthMaterialClass.html)

### Notes: 
The nt file was saved in turtle format (using Protégé) for better human readability. Classes are skos:Concepts. There are two namespaces, one for RockNames, which appear to apply to individual, mostly hand-sample scale rock classification, and RockComposite -- composite classes with multiple rock types, which would seem to apply to outcrop or map unit scale lithology. Both are included in a single skos:ConceptScheme.

### [BGSRockName.ttl](https://github.com/smrgeoinfo/vocabulary/blob/main/lithology/BGSRockName.ttl)
skos:broader and skos:narrower relations in the RockName namespace denote a subsumption (IsA) hierarchy. In the RockComposite namespace, it appears that skos:narrower denotes ‘isPartOf’, and skso:broader denotes ‘hasPart’. For example _Mud has narrower ‘Gravel, sand and mud’_. _‘Gravel, sand and mud’ has broader Gravel_.  Thus displaying the hierarchy for the full concept scheme using the skos relations leads to incoherent results.  To address this, the RockName namespace was extracted (SPARQL query, TopBraid composer), to produce ‘BGSRockName.ttl’. The skos:broader relations in this extract produce a reasonable hierarchy.  There are 3022 skos:Concept instances in this ontology, with mostly hand-sample scale classes.

## [GSO_Geologic_Rock_Material.ttl](https://github.com/smrgeoinfo/vocabulary/blob/main/lithology/GSO-Geologic_Rock_Material.ttl)
This is an owl ontology module in the GSO ontology, with hand-sample scale material types represented as owl:Class.  Hierarchy is represented with owl:subClassOf relations. This classification is inherited from the CGI Simple_Lithology vocabulary (some info at 10.5281/zenodo.7412250.), with the skos:Concept converted to owl:Class, and skos:broader converted to owl:subClassOf. The top Concept is gsog:Rock_Material, which is imported from another ontology module in the GSO ontology (DOI: 10.5281/zenodo.4750707).   Some classes have been added based on requirements discovered working with the Loop3D and other projects. There are ~300 classes. Sources for definitions are cited with dcterms:source. [Hosted on Github](https://github.com/Loop3D/GKM/blob/master/Loop3D-GSO/Modules/GSO-Geologic_Rock_Material.ttl)
