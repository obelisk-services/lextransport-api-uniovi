from sqlmodel import Field, Relationship, Session, SQLModel, select, Index
from pydantic import EmailStr
from datetime import datetime



class Contrato(SQLModel):
    LicTradNum: str
    CstmrCode : str
    CstmrName: str
    ContractID: int
    CntrcTmplt: str
    Remarks1: str | None
    StartDate: datetime
    EndDate: datetime
    Status: str
    Lines: list["LineaContrato"]

class LineaContrato(SQLModel):
    #ContractID: int = Field(nullable=False )
    Line: int
    ManufSN: str
    U_tipo: str | None
    StartDate: datetime
    EndDate: datetime