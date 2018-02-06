{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% for _ in cookiecutter.project_name %}#{% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}#{% endfor %}

{% if is_open_source %}
.. image:: https://img.shields.io/travis/Nekmo/{{ cookiecutter.project_name }}.svg?style=flat-square&maxAge=2592000
  :target: https://travis-ci.org/Nekmo/{{ cookiecutter.project_name }}
  :alt: Latest Travis CI build status

.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_name }}.svg?style=flat-square
  :target: https://pypi.org/project/{{ cookiecutter.project_name }}/
  :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_name }}.svg?style=flat-square
  :target: https://pypi.org/project/{{ cookiecutter.project_name }}/
  :alt: Python versions

.. image:: https://img.shields.io/codeclimate/github/Nekmo/{{ cookiecutter.project_name }}.svg?style=flat-square
  :target: https://codeclimate.com/github/Nekmo/{{ cookiecutter.project_name }}
  :alt: Code Climate

.. image:: https://img.shields.io/codecov/c/github/Nekmo/{{ cookiecutter.project_name }}/master.svg?style=flat-square
  :target: https://codecov.io/github/Nekmo/{{ cookiecutter.project_name }}
  :alt: Test coverage

.. image:: https://img.shields.io/requires/github/Nekmo/{{ cookiecutter.project_name }}.svg?style=flat-square
     :target: https://requires.io/github/Nekmo/{{ cookiecutter.project_name }}/requirements/?branch=master
     :alt: Requirements Status
{%- endif %}


{{ cookiecutter.project_short_description }}


To install {{ cookiecutter.project_name }}, run this command in your terminal:

.. code-block:: console

    $ sudo pip install {{ cookiecutter.project_name }}

This is the preferred method to install {{ cookiecutter.project_name }}, as it will always install the most recent stable release.


Features
========

* TODO

