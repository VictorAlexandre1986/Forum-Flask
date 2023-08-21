import uuid as uuid
from datetime import datetime

import uuid as uuid
from sqlalchemy import VARCHAR, Column, Integer, DateTime, UUID
from sqlalchemy.ext.declarative import declarative_base


class BaseModel:

    id = Column(Integer, primary_key=True)
    uuid = Column(VARCHAR, primary_key=True, default=uuid.uuid4)
    date_create = Column(DateTime(timezone=True), default=datetime.utcnow, nullable=False)
    date_update = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


Base = declarative_base(cls=BaseModel)