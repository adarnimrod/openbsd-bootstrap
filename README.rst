OpenBSD bootstrap
#################

.. image:: https://travis-ci.org/adarnimrod/openbsd-bootstrap.svg?branch=master
    :target: https://travis-ci.org/adarnimrod/openbsd-bootstrap

Role to bootstrap an OpenBSD instance (allow Ansible to provision the instance).

Requirements
------------

See :code:`meta/main.yml` and assertions at the top of :code:`tasks/main.yml`.

Role Variables
--------------

See :code:`defaults/main.yml`.

Dependencies
------------

See :code:`meta/main.yml`.

Example Playbook
----------------

See :code:`tests/playbook.yml`.

Testing
-------

Testing requires Python 2.7 and either Docker or Vagrant and Virtualbox.
Install the Python dependencies, dependent roles and roles required for
testing:

.. code:: shell

    pip install -r tests/requirements.txt
    ansible-galaxy install git+file://$(pwd),$(git rev-parse --abbrev-ref HEAD) -p .molecule/roles
    molecule dependency

To run the full test suite:

.. code:: shell

    pre-commit run --all-files
    molecule test --platform all

License
-------

This software is licensed under the MIT license (see the :code:`LICENSE.txt`
file).

Author Information
------------------

Nimrod Adar, `contact me <nimrod@shore.co.il>`_ or visit my `website
<https://www.shore.co.il/>`_. Patches are welcome via `git send-email
<http://git-scm.com/book/en/v2/Git-Commands-Email>`_. The repository is located
at: https://www.shore.co.il/git/.
