neb
==============

## Description

neb is a Python library for accessing Trinity, the standalone Python
[Neo4j](http://neo4j.org) server.


## Python Dependencies

* restkit >= 2.1.1

## Usage

Trinity doesn't support authentication, so this is a really simple interface.

### Create a node, if it doesn't already exist

    import neb.node
    data = {'username': 'bueda', 'user_id': 12345}
    neb.node.Node().create(node_id='bueda', node=data)

### Create a relationship between two nodes

Without having to have either node loaded:

    import neb.relationship
    data = {'since': '09/20/09'}
    neb.relationship.Relationship().create(start='bueda', to='peplin',
            type='works_for', **data)

Or, if you already have one of the nodes:

    import neb.node
    data = {'username': 'bueda', 'user_id': 12345}
    node = neb.node.Node().create(node_id='bueda', **data)

    data = {'since': '09/20/09'}
    node.connect(to='peplin', type='works_for', **data)

Or, if you already have both of the nodes:

    import neb.node
    data = {'username': 'bueda', 'user_id': 12345}
    employer = neb.node.Node().create(node_id='bueda', **data)

    data = {'username': 'peplin', 'user_id': 78910}
    employee = neb.node.Node().create(node_id='peplin', **data)

    data = {'since': '09/20/09'}
    employee.connect(to=employer, type='works_for', **data)

### Retreive node statistics

The stats method is relatively free form, and depends on what the specific
instance of Trinity offers. In this case, assume it has a 'topics' node
statistic.

    import neb.statistic 
    neb.statistic.Statistic().calculate(node_id='bueda', stat='topics')

If you have the node instance already:

    import neb.node
    data = {'username': 'bueda', 'user_id': 12345}
    node = neb.node.Node().create(node_id='bueda', **data)
    node.statistic(stat='topics')
