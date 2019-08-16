from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = 'pyverbal',
    packages = [
        'pyverbal', 
        'pyverbal.conjugation', 
        'pyverbal.lang'
    ],
    version = '1.0.0',
    description = 'Verbs conjugation and desconjugation',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author = 'metadeta96',
    author_email = 'metadeta96@gmail.com',
    url = 'https://github.com/metadeta96/pyverbal',
    download_url = 'https://github.com/metadeta96/pyverbal',
    keywords = [
        'verbs', 
        'grammar', 
        'conjugation', 
        'pt-br', 
        'pt',
        'portugues',
        'portuguese',
        'gramatica',
        'verbal',
        'conjugacao'
    ],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
    ],
    install_requires=['pyyaml'],
    python_requires='>=3.6',
    package_data={
        'pyverbal': ['data/**/*.yaml']
    }
)