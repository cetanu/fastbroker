FastBroker
==========

A project built on FastAPI that aims to provide an easy framework for building Open Service Brokers.

TODO
====

0. ~~Build empty endpoints that match the OSB OpenAPI spec~~
0. Fill in endpoints with OSB workflow code
0. Add abstract classes for adding service/plans and building out the catalog in an auto-discovered way
0. Background tasks for async operations
0. More advanced async task backends AKA allow choosing a broker/execution engine (eg. celery/dramatiq/other)
0. Pluggable data persistence aka allow choosing between DB backends
