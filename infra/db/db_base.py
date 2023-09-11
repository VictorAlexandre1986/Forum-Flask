import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, UUID, BigInteger, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

class BaseModel:
    
    id = Column(BigInteger(), primary_key=True)
    # uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # uuid = Column(VARCHAR, primary_key=True, default=uuid.uuid4)
    date_create = Column(DateTime(timezone=True), default=datetime.utcnow, nullable=False)
    update_create = Column(DateTime(timezone=True), default=datetime.utcnow, nullable=False)
    
    
    
Base = declarative_base(cls=BaseModel)