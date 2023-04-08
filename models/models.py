from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey
from datetime import datetime

metadata = MetaData()

software = Table(
    "software",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("version", String, nullable=False)
)
