from rdflib import Graph
from rdflib import BNode, URIRef,Literal
from rdflib import Namespace
import pprint
import rdflib

n = Namespace("http://teaManagement/")
g = Graph()

tea=URIRef("http://teaManagement/tea")
supplier=URIRef("http://teaManagement/supplier")
variety=URIRef("http://teaManagement/variety")
whitetea=URIRef("http://teaManagement/whitetea")
greentea=URIRef("http://teaManagement/greentea")
blacktea=URIRef("http://teaManagement/blacktea")
scentedtea=URIRef("http://teaManagement/scentedtea")
shop=URIRef("http://teaManagement/shop")
customer=URIRef("http://teaManagement/customer")
factory=URIRef("http://teaManagement/factory")
teashops=URIRef("http://teaManagement/teashops")
Manager=URIRef("http://teaManagement/Manager")
Order=URIRef("http://teaManagement/Order")


purchased_by = URIRef("http://teaManagement/purchased_by")
has= URIRef("http://teaManagement/has")
is_of_type=URIRef("http://teaManagement/is_of_type")
rich_in=URIRef("http://teaManagement/rich_in")
protect_aganist=URIRef("http://teaManagement/protect_aganist")
lowers_bad=URIRef("http://teaManagement/lowers_bad")
helps_to_relax=URIRef("http://teaManagement/helps_to_relax")
distributes_to=URIRef("http://teaManagement/distributes_to")
buys_from=URIRef("http://teaManagement/buys_from")
processed_in=URIRef("http://teaManagement/processed_in")
pays_bill_to=URIRef("http://teaManagement/pays_bill_to")
taken_by=URIRef("http://teaManagement/taken_by")
gives=URIRef("http://teaManagement/gives")


g.add((tea,purchased_by,supplier))
g.add((tea,has,variety))
g.add((variety,is_of_type,whitetea))
g.add((variety,is_of_type,greentea))
g.add((variety,is_of_type,blacktea))
g.add((variety,is_of_type,scentedtea))
g.add((whitetea,rich_in,Literal("Antioxidants")))
g.add((greentea,protect_aganist,Literal("cancer")))
g.add((blacktea,lowers_bad,Literal("cholestrol")))
g.add((scentedtea,helps_to_relax,Literal("Muscles")))
g.add((supplier,distributes_to,shop))
g.add((shop,distributes_to,Literal("hotels")))
g.add((customer,buys_from,shop))
g.add((tea,processed_in,factory))
g.add((factory,distributes_to,teashops))
g.add((teashops,has,Manager))
g.add((customer,pays_bill_to,Manager))
g.add((Order,taken_by,Manager))
g.add((Order,taken_by,Literal("Waiter")))
g.add((customer,gives,Order))


for s in g:
    pprint.pprint(s)
print(len(g))

# navigation 
for s, p, o in g:
    if not (s, p, o) in g:
        raise Exception("Iterator / Container Protocols are Broken!!")


# check operations    
if (tea, None, None) in g:
    print("This graph contains triples about TEA!") 


# Set theoretic operations
g1 = rdflib.Graph()
g1.add((Order,taken_by,Manager))
g1.add((Order,taken_by,Literal("Waiter")))
print(len(g1))

g2 = rdflib.Graph()
g2=g+g1
print("g+g1 Graph:")
print(len(g2))

g3 = rdflib.Graph()
g3=g-g1
print("g-g1 Graph:")
print(len(g3))


# Graph Methods
g4= rdflib.Graph()
g4=g.subjects(predicate=has, object=variety)
for s in g4:
    print("%s" %s)
g5= rdflib.Graph()
g5= g.predicate_objects(subject=tea)
for s in g5:
    print(s)


#SPARQL queries
g.serialize(destination='output.xml',format='xml')
g6=Graph()
g6.parse("output.xml")
qres=g6.query(
""" SELECT ?s

{
?s
<http://teaManagement/is_of_type>
<http://teaManagement/greentea>


}"""
)
for row in qres:
    print("%s" %row)



qres=g6.query(
"""ASK { <http://teaManagement/tea> <http://teaManagement/purchased_by> <http://teaManagement/supplier>}"""
)

for row in qres:
    print("%s" %row)