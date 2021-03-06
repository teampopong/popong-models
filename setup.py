from setuptools import setup

setup(
    name='popong_models',
    version='0.1.0-dev',
    url='http://github.com/teampopong/popong_models/',
    license='BSD',
    author='Cheol Kang',
    author_email='steel@popong.com',
    description='A Korean political data models made by '
                'team POPONG',
    packages=['popong_models'],
    platforms='any',
    scripts=['popong_models/bin/popong-alembic-init'],
    include_package_data=True,
    install_requires=[
        'alembic>=0.5.0',
        'SQLAlchemy>=0.8.1',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
