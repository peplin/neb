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

Use neb to notify Hoptoad of an app deploy::

    import hoppy.deploy
    hoppy.api_key = '<project API key>'
    hoppy.deploy.Deploy().deploy(env='PRODUCTION', scm_revision='1a6a445',
            scm_repository='git@github.com:peplin/hoppy.git')

Use hoppy to retreive a specific error::

    import hoppy.error
    hoppy.account = '<your account name>'
    hoppy.auth_token = '<your personal API auth token>'
    print hoppy.error.Error().find(2035230).environment
