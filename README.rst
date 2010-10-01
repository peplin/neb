neb
==============

.. _Python: http://python.org/
.. _restkit: http://benoitc.github.com/restkit/
.. _neo4j: http://neo4j.org/

neb is a Python library for accessing Trinity, the standalone Python neo4j_
server.


Requirements
------------

hoppy requires:

* Python_ 2.6
* restkit_ >= 2.1.1


Usage
-----

Trinity doesn't support authentication, so this is a really simple interface.

Use neb to retreive a specific node::

    import neb.error
    print neb.node.Node().find(2035230)
