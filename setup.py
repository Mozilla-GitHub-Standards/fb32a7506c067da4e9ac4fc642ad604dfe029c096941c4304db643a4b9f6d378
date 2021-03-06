from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()
with open('requirements_test.txt') as f:
    test_requirements = f.read().splitlines()

setup(
    # Meta
    author='Steven Englehardt',
    author_email='senglehardt@mozilla.com',
    description='Tools for parsing crawl data generated by OpenWPM',
    name='openwpm-utils',
    license='MPL 2.0',
    url='https://github.com/mozilla/openwpm-utils',
    version='0.1.2',
    packages=['openwpm_utils'],

    # Dependencies
    install_requires=requirements,
    tests_require=test_requirements,
    setup_requires=['setuptools_scm', 'pytest-runner'],

    # Packaging
    include_package_data=True,
    use_scm_version=False,
    zip_safe=False,

    # Classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment :: Mozilla',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Scientific/Engineering :: Information Analysis'
    ],
)
