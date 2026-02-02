from sqlalchemy.exc import SQLAlchemyError

class DatabaseError(Exception):
    pass

class TMDBError(Exception):
    pass
