Example
#######

An (empty) example Ansible role complete with working tests out of the box. For
more information read the `blog post
<https://www.shore.co.il/blog/ansible-example-role/>`_.

Requirements
------------

See :code:`meta/main.yml`, :code:`requirements.yml` and assertions at top of
:code:`tasks/main.yml`.

Adding the role as a dependency
-------------------------------

Add the following to your :code:`meta/main.yml`:

.. code:: yaml

    dependencies:
    - src: https://www.shore.co.il/git/ansible-role-example
      scm: git
      name: example

When :code: `ansible-galaxy` downloads your role it will also download its
dependencies, ensuring this role will be present and run everytime your role
runs.

Adding the role to your playbooks
---------------------------------

Add the following to your :code:`requirements.yml`:

.. code:: yaml

    - src: https://www.shore.co.il/git/ansible-role-example
      scm: git
      name: example

and update your roles by running :code: `ansible-galaxy install -r
requirements.yml`.

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

Testing requires Virtualbox and Vagrant (out of scope for this documentation).
Install the Python dependencies, add pre-commit hooks by running:

.. code:: shell

    pip install -r tests/requirements.txt
    pre-commit install

To run the full test suite:

.. code:: shell

    ansible-galaxy install git+file://$(pwd),$(git rev-parse --abbrev-ref HEAD) -p .molecule/roles
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
