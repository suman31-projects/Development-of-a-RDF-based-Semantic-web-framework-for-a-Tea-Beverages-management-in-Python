# Development-of-a-RDF-based-Semantic-web-framework-for-a-Tea-Beverages-management-in-Python
The Semantic Web is an extension of the World Wide Web through standards set by the World Wide Web Consortium (W3C). The goal of the Semantic Web is to make Internet data machine-readable. 
To enable the encoding of semantics with the data, technologies such as 
1] Resource Description Framework (RDF) and 
2] Web Ontology Language (OWL) are used

GOAL-->Make computers to understand about the search 

Semantic web used in,
Auto suggest your webpages
Videos[YouTube]
Jobs[LinkedIn]

Machine Accessible Content
For example if we have a sentence “I am a philosopher, you may think” but today’s web only catch the keywords like philosopher and give related links to that but it will never do interpretation of the sentence

RDF-Resource Description Framework
Standard given by W3C
Used to give semantic information about web pages
It creates relationship with documents
RDF consists of triplets
< Subject, Property/Predicate, Object >
< Mozart, Composed, the Magic Flute >
To link Subject and Object Property is used
Here whatever in web pages all are in triplet format

In RDF readily available domain(vocabulary) is used
Eg: RDF/XML, N3, NTriples, N-Quads, Turtle
In web pages RDF is used in meta tag (where description of a tag is used) 
In RDF subject may be the object in triplet combination vice-versa

Resources;
Every resources has URI(Uniform Resource Identifier)
A  URI can be a URL(web address) or some other kind of identifier
A identifier does not necessarily enable access to a resource
Eg: People, places, things

Properties;
They are special kind of resources 
They describe relationship between resources
Eg: written by, composed by, title
Properties/Predicate in RDF are identified by URI

Statement: -
A statement is an object-attribute-value triple
It consists of Subject-Property-Object 
Eg: Book--------------->MIT press

Querying RDF data: -
Querying languages such as SPAQL(Subject, Predicate, Object combination)
It’s only about linking those triples
Creating Subject and relating it with Object and Predicate
Each node is subject and have direction to connect predicate and objects

Most forms of query language contain a set of triple patterns
Triple patterns are same where subject, predicate and object is a variable given during runtime

Drawbacks;
No precisely described meaning is embedded in it
No logical inference can be drawn

RDF are also called as Web AI
Security will be given by cryptography
Python supports RDF ( it has functions)

RDFLib: -
Pure python package used for working with RDF
RDFLib graphs are built-in python methods in order to behave in predictable way
RDF graphs cannot be sorted they have only set operations
Eg: g.add( ) is used to add triples 

Syntax;
{
(Subject0,Predicate0,Object0)
……………………………….
(SubjectN,PredicateN,ObjectN)
}

Creating Nodes: -
RDF data is a graph where the nodes are URI references, Blank Nodes or Literals. 
In RDFLib, these node types are represented by the classes URIRef, BNode, and Literal.
A BNode is a node where the exact URI is not known. 
A URIRef is a node where the exact URI is known, URIRef are also used to represent the properties/predicates in the RDF graph.
Literals represent attribute values, such as a name, a date, a number, etc. e.g. string, int…

Eg: bob = URIRef("http://example.org/people/Bob") 
       linda = BNode() # a GUID is generated
       name = Literal('Bob') # passing a string 
       age = Literal(24) # passing a python int

1] Navigating Graphs: -
An RDF Graph is a set of RDF triples(Subject, Predicate, Object)
The Python Graph() tries to emulate a container type(checking if particular triplet is there in graph or not)
Syntax;
for subject, predicate, object in someGraph:
 	if not (subject, predicate, object) in someGraph: 
		raise Exception("Iterator / Container Protocols are Broken!!")

2] Check Operation: -
 To check if a triple is in a graph 
Syntax;
if (bob, RDF.type, FOAF.Person) in graph:
	 print("This graph knows that Bob is a person!")
   
   
3] Set Operations on RDFLib Graphs: -
Operations that cam be performed on graphs
G1 + G2 return new graph with union(duplicates will not come)
G1 - G2 return new graph with difference

Syntax;
if (result == "gAndg1"):
   g2 = rdflib.Graph()
   g2=g+g1

4] Graph methods : -
These are used for accessing any of the triples
Syntax;
for s,p,o in g.predicates( (subject=None,object=None) ):
	 print("%s is a %s"%(s,o))

In the above example predicate needs to be searched as input query and subject, object combination will be rendered

5] SPARQL Queries: - 
Select subject and predicate to get the object of that triplet
Syntax;
x="<http://teaManagement/"+s+">"
y="<http://teaManagement/"+p+">"
sel= "SELECT ?o { "+x+" "+y+" "+"?o }"
print(sel)


















