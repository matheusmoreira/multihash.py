import setuptools

def read(path: str) -> str:
    with open(path, 'r') as file:
        return file.read()

def README() -> str:
    return read('README.md')

def version() -> str:
    return read('version').strip()

setuptools.setup(
    name='multi-hash',
    version=version(),
    author='Matheus Afonso Martins Moreira',
    author_email='matheus.a.m.moreira@gmail.com',
    description='Self-describing hashes',
    long_description=README(),
    long_description_content_type='text/markdown',
    url='https://github.com/matheusmoreira/multihash.py',
    packages=['multihash'],
    package_data={'multihash': ['py.typed', '*.pyi']},
    install_requires=['uvarint>=1.2,<2'],
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Typing :: Typed',
    ],
)
