import datetime
from sqlalchemy import BigInteger
from sqlalchemy import Column
from sqlalchemy import MetaData
from sqlalchemy import String
from sqlalchemy import text
from sqlalchemy import TIMESTAMP
from sqlalchemy import Date
from sqlalchemy.ext.declarative import declarative_base

customers_metadata = MetaData(schema="customers")
CustomersBase = declarative_base(metadata=customers_metadata)


class Customers(CustomersBase):
    __tablename__ = "customers"

    id = Column(BigInteger, primary_key=True, server_default=text("'0'"), autoincrement=True)
    des_name = Column(String(250))
    # Verificar guardar automáticamente la fecha actual
    # date_creation_a = Column(Date, nullable=False, server_default=text("CURRENT_TIMESTAMP")) # Wrong, error when running the migration, invalid. syntax.
    # date_creation_b = Column(Date, nullable=False, server_default=text("now()")) # Wrong, error when running the migration, invalid. syntax.
    date_creation_c = Column(Date, nullable=False, server_default=text("(now())"))
    # Analyze how to create `on update` without a default value. I need to create `date_updated timestamp null on update CURRENT_TIMESTAMP`
    date_updated_a = Column(TIMESTAMP, onupdate=datetime.datetime.now) # Wrong, creates `date_updated_a TIMESTAMP NULL,`
    date_updated_b = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")) # Wrong, creates `date_updated_b TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,`
    # date_updated_c = Column(TIMESTAMP, server_default=text("ON UPDATE CURRENT_TIMESTAMP")) # Wrong, creates `date_updated_c TIMESTAMP NULL DEFAULT ON UPDATE CURRENT_TIMESTAMP,`. Invalid sql syntax
    # date_updated_d = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE")) # Wrong, creates `date_updated_d TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE,`. Invalid sql syntax
    date_updated_e = Column(TIMESTAMP, server_default=text("null ON UPDATE CURRENT_TIMESTAMP")) # Ok, creates `date_updated_e timestamp null on update CURRENT_TIMESTAMP`
