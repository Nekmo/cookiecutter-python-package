#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""
import os
import uuid

import sys
from setuptools import setup, find_packages
from pip.req import parse_requirements

__dir__ = os.path.abspath(os.path.dirname(__file__))
scripts_path = os.path.join(__dir__, 'scripts')


def get_url(ir):
    if hasattr(ir, 'url'): return ir.url
    if ir.link is None: return
    return ir.link.url


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()


# Requirements list
requirements_path = os.path.join(__dir__, 'py{}-requirements.txt'.format(sys.version_info.major))
if os.path.exists(requirements_path):
    requirements = parse_requirements(requirements_path, session=uuid.uuid1())
    install_requires = [str(ir.req) for ir in requirements if not get_url(ir)]
    dependency_links = [get_url(ir) for ir in requirements if get_url(ir)]
else:
    install_requires = []
    dependency_links = []


setup_requirements = [
{%- if cookiecutter.use_pytest == 'y' %}
    'pytest-runner',
{%- endif %}
    # TODO({{ cookiecutter.github_username }}): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
{%- if cookiecutter.use_pytest == 'y' %}
    'pytest',
{%- endif %}
    # TODO: put package test requirements here
]

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

if os.path.exists(scripts_path):
    scripts_dir_name = scripts_path.replace(__dir__, '', 1)
    scripts_dir_name = scripts_dir_name[1:] if scripts_dir_name.startswith(os.sep) else scripts_dir_name
    scripts = [os.path.join(scripts_dir_name, file) for file in os.listdir(scripts_path)]
else:
    scripts = []


packages = find_packages(__dir__)
# Prevent include symbolic links
for package in tuple(packages):
    path = os.path.join(__dir__, package.replace('.', '/'))
    if not os.path.exists(path):
        continue
    if not os.path.islink(path):
        continue
    packages.remove(package)


modules = list(filter(lambda x: '.' not in x, packages))

package_version = __import__(modules[0]).__version__


setup(
    name='{{ cookiecutter.project_name }}',
    version=package_version,
    description="{{ cookiecutter.project_short_description }}",
    long_description=readme + '\n\n' + history,
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    packages=modules,
    include_package_data=True,
    install_requires=install_requires,
    dependency_links=dependency_links,
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    zip_safe=False,
    keywords='{{ cookiecutter.project_slug }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
{%- if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
{%- endif %}
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
    scripts = scripts,
)
