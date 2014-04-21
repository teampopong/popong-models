# POPONG Models

A set of data models for Korean political data written in SQLAlchemy.
These models extract valuable information of Korean politics, and power [Pokr](http://pokr.kr) and [POPONG APIs](http://data.popong.com).

## Usage

Initialize new database:

    $ cd PROJECT_DIRECTORY
    $ popong-alembic-init
    $ vi alembic.ini       # fill database location


Python models:

    #!/usr/bin/env python
    
    from popong_models import Person
    some_people = Person.query.filter_by(birthday_month=3).all()

