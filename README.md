# knowledge-systems-and-technology

The project of the class Knowledge Systems and Technologies 2019-2020 of ECE NTUA.

This project is about the creation of an ontology about the transport means. The ontology is very wide, however we didn't have the respective data so in the implementation we used only data regarding the bus, subways and trolleys in Athens. For this section we used the GTFS prototype and enriched it with more classes and data properties.

We did the impremenation using the tool Protege and we divided the classes between publc and private transport means.
We added the  domains, ranges and the object properties. Then we created, through Protege, the owl code.

We turned the csv files to RDF triples and as a represantation we used N-triples. This procedure took place by using Python code. We also tried to prduce meta-knowledge.

In the end we used the Virtuoso tool, through which we connected the previous results, meaning the owl code and the RDF triples. Thus we create our graph of knowledge and run some SPARQL queries.
