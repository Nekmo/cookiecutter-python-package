Welcome to {{ cookiecutter.project_name }}'s documentation!
======================================
{{ cookiecutter.project_short_description }}

To **install** {{ cookiecutter.project_name }}, run this command in your terminal:

.. code-block:: console

    $ pip install amazon_dash


Contents
--------

.. toctree::
   :maxdepth: 3

   readme
   installation
   usage
   troubleshooting
   modules
   contributing
   {% if cookiecutter.create_author_file == 'y' -%}authors
   {% endif -%}history

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
