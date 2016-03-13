OpenBSD bootstrap
#################

Role to bootstrap an OpenBSD instance (allow Ansible to provision the instance).

Requirements
------------

OpenBSD 5.7 or later.

Role Variables
--------------

.. code:: yaml

    openbsd_pkg_mirror: http://www.mirrorservice.org/pub #OpenBSD mirror to use.

Dependencies
------------

None.

Example Playbook
----------------
.. code:: yaml

    ---
    - hosts: all
      gather_facts: False
      roles:
      - ansible-role-openbsd-bootstrap

Example requirements.yml
------------------------
.. code:: yaml

    ---
    - src: https://www.shore.co.il/git/ansible-role-openbsd-bootstrap
      scm: git
      path: roles/
      name: openbsd-bootsrrap

License
-------

This software is licensed under the MIT license (see the :code:`LICENSE.txt`
file).

Testing
-------

Testing is done with `Molecule <https://molecule.readthedocs.org/>`_. Also, this
repository has `pre-commit <http://pre-commit.com/>`_ configured.

Author Information
------------------

Nimrod Adar, `contact me <nimrod@shore.co.il>`_ or visit my `website
<https://www.shore.co.il/>`_. Patches are welcome via `git send-email
<http://git-scm.com/book/en/v2/Git-Commands-Email>`_. The repository is located
at: https://www.shore.co.il/git/.
