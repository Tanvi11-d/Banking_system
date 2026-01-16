from database import engine
from sqlalchemy.orm import DeclarativeBase,mapped_column,Mapped,relationship
from sqlalchemy import String,Float,ForeignKey
from sqlalchemy.ext.mutable import MutableList

class Base(DeclarativeBase):
    pass

class Account(Base):
    __tablename__="account"

    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String,nullable=False)
    email:Mapped[str]=mapped_column(String,nullable=False)
    age:Mapped[str]=mapped_column(String,nullable=False)
    city:Mapped[str]=mapped_column(String,nullable=False)
    balance:Mapped[float]=mapped_column(Float)
    transaction_ref:Mapped[MutableList['Transaction']]=relationship('Transaction',back_populates="account_ref", cascade="all,delete")

   
        
    def __repr__(self):
            return f"<account_id:{self.id} account_holder_name:{self.name} Email:{self.email} Age:{self.age} City:{self.city} Balance:{self.balance}>"
    
class Transaction(Base):
    __tablename__="transaction"

    id:Mapped[int]=mapped_column(primary_key=True)
    amount:Mapped[float]=mapped_column(Float)
    type:Mapped[str]=mapped_column(String)
    account_id:Mapped[int]=mapped_column(ForeignKey('account.id'))
    account_ref:Mapped[MutableList[Account]]=relationship('Account',back_populates="transaction_ref")

    def __repr__(self):
        return f"<transaction_id:{self.id} amount:{self.amount} type:{self.type} account_id:{self.account_id}>"


  
def create_table():
     Base.metadata.create_all(engine)

    





