# POPONG Models

A set of data models for Korean political data written in SQLAlchemy.
These models extract valuable information of Korean politics, and power [Pokr](http://pokr.kr) and [POPONG APIs](http://data.popong.com).

## Install

    $ sudo pip install git+https://github.com/teampopong/popong-models.git

## Usage

Initialize new database:

    $ cd PROJECT_DIRECTORY
    $ popong-alembic-init
    $ vi alembic.ini       # fill database location


Python models:

    #!/usr/bin/env python
    
    from popong_models import Person
    some_people = Person.query.filter_by(birthday_month=3).all()

