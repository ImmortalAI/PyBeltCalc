from re import M
from unittest import result
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Table_1_8(Base):
    __tablename__ = 'table_1_8'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    HN: Mapped[str] = mapped_column()
    TM: Mapped[str] = mapped_column()
    TD: Mapped[str] = mapped_column()
    C3: Mapped[float] = mapped_column()

class Table_2_1(Base):
    __tablename__ = 'table_2_1'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    profil: Mapped[str] = mapped_column(index=True)
    record: Mapped[str] = mapped_column()
    value: Mapped[float] = mapped_column()

class Table_2_4(Base):
    __tablename__ = 'table_2_4'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    alpha1: Mapped[float] = mapped_column(index=True)
    C1: Mapped[float] = mapped_column()
    
class Table_2_7(Base):
    __tablename__ = 'table_2_7'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    profil: Mapped[str] = mapped_column(index=True)
    DP1: Mapped[float] = mapped_column()
    V: Mapped[float] = mapped_column()
    DF0: Mapped[float] = mapped_column()
    
class Table_2_8(Base):
    __tablename__ = 'table_2_8'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    profil: Mapped[str] = mapped_column(index=True)
    u: Mapped[float] = mapped_column(index=True)
    dDFi: Mapped[float] = mapped_column()
    
class Table_2_9(Base):
    __tablename__ = 'table_2_9'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    profil: Mapped[str] = mapped_column(index=True)
    L0: Mapped[float] = mapped_column()
    LL0: Mapped[float] = mapped_column()
    CL: Mapped[float] = mapped_column()

class Unit(Base):
    __tablename__ = 'unit'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    HN: Mapped[str] = mapped_column()
    TM: Mapped[str] = mapped_column()
    TD: Mapped[str] = mapped_column()
    
class AssemblyUnit(Base):
    __tablename__ = 'assembly_unit'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    unit_id: Mapped[int] = mapped_column(ForeignKey('unit.id'))
    unit: Mapped[Unit] = relationship()
    
    NSE: Mapped[str] = mapped_column()
    TSE: Mapped[str] = mapped_column()
    VSE: Mapped[str] = mapped_column()
    F: Mapped[float] = mapped_column()
    Z: Mapped[float] = mapped_column()
    DF: Mapped[float] = mapped_column()
    u: Mapped[float] = mapped_column()
    DF0: Mapped[float] = mapped_column()
    NV: Mapped[float] = mapped_column()
    dDFi: Mapped[float] = mapped_column()
    dDF0: Mapped[float] = mapped_column()
    C3: Mapped[float] = mapped_column()
    N: Mapped[float] = mapped_column()
    
class Part(Base):
    __tablename__ = 'part'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    assembly_unit_id: Mapped[int] = mapped_column(ForeignKey('assembly_unit.id'))
    assembly_unit: Mapped[AssemblyUnit] = relationship()
    
    ND: Mapped[str] = mapped_column()
    DP1:Mapped[float] = mapped_column(nullable=True)
    V: Mapped[float] = mapped_column(nullable=True)
    S10: Mapped[float] = mapped_column(nullable=True)
    alpha1: Mapped[float] = mapped_column(nullable=True)
    L0: Mapped[float] = mapped_column(nullable=True)
    C1: Mapped[float] = mapped_column(nullable=True)
    L: Mapped[float] = mapped_column(nullable=True)
    CL: Mapped[float] = mapped_column(nullable=True)
    profil: Mapped[str] = mapped_column(nullable=True)
    LL0: Mapped[float] = mapped_column(nullable=True)