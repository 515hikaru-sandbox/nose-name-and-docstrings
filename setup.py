from setuptools import setup

setup(
    name='nose-custom-docstring',
    version='0.1',
    description='Custom docstring to name tests in nose.',
    keywords='nose testing',
    author='Marc Schlaich',
    author_email='karanodeny@gmail.com',
    url='https://github.com/515hikaru/nose-custom-docstring',
    license='MIT',
    py_modules=['nose_customdoc'],
    zip_safe=False,
    entry_points={
        'nose.plugins': [
            'nose_customdoc = nose_customdoc:CustomDocstrings',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
