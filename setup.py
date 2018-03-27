from setuptools import setup

setup(
    name='nose-name-and-docstrings',
    version='0.1',
    description='Show docstring with test name in nose.',
    keywords='nose testing',
    author='515hikaru',
    author_email='karanodeny@gmail.com',
    url='https://github.com/515hikaru/nose-name-and-docstring',
    license='MIT',
    py_modules=['nose_name_and_docstrings'],
    zip_safe=False,
    entry_points={
        'nose.plugins': [
            'nose_name_and_docstrings = nose_name_and_docstrings:NameWithDocstrings',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
