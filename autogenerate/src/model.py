import datetime
from sqlalchemy import BigInteger
from sqlalchemy import Column
from sqlalchemy import MetaData
from sqlalchemy import String
from sqlalchemy import text
from sqlalchemy import TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

customers_metadata = MetaData(schema="customers")
CustomersBase = declarative_base(metadata=customers_metadata)


class Customers(CustomersBase):
    __tablename__ = "customers"

    id = Column(BigInteger, primary_key=True, server_default=text("'0'"), autoincrement=True)
    des_name = Column(String(250))
    # date_updated = Column(TIMESTAMP, onupdate=datetime.datetime.now) # Does not work. Alembic does not create the autoincrement
    date_updated = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")) # Does not work. Alembic generates `date_updated timestamp default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP` but i only want `date_updated timestamp null on update CURRENT_TIMESTAMP`
