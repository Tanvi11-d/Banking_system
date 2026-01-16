from services import create_accounts,get_all_accounts,get_accounts,update_accounts,delete_accounts,deposits,get_transcations,get_all_transcations,withdraws
from database import Sessionlocal
from sqlalchemy.orm import Session
from models import create_table
from schema import accountcreate,accountout,accountupdate,transaction,transactionout
from fastapi import FastAPI,Depends,status

app=FastAPI()

create_table()


def get_db():
    db=Sessionlocal()
    try:
        yield db
    finally:
        db.close()


# create account
@app.post("/account/",response_model=accountout,status_code=status.HTTP_201_CREATED)
def create_account(accounts:accountcreate,db:Session = Depends(get_db)):
   return create_accounts(db,accounts)

# fetch all records
@app.get("/account/",response_model=list[accountout],status_code=status.HTTP_200_OK)
def get_all_account(db:Session=Depends(get_db)):
    return get_all_accounts(db)


# fetch records
@app.get("/account/{account_id}",response_model=accountout,status_code=status.HTTP_200_OK)
def get_account(account_id:int,db:Session=Depends(get_db)):
    return get_accounts(db,account_id)


#update account
@app.put("/account/{account_id}",response_model=accountout,status_code=status.HTTP_200_OK)
def update_account(account_id:int,accounts:accountupdate,db:Session=Depends(get_db)):
    return update_accounts(db,account_id,accounts)

# Delete account
@app.delete("/account/{account_id}",response_model=accountout,status_code=status.HTTP_200_OK)
def delete_account(account_id:int,db:Session=Depends(get_db)):
    return delete_accounts(db,account_id)

# Deposit
@app.post("/account/deposit/{account_id}",response_model=transactionout,status_code=status.HTTP_201_CREATED)
def deposit(account_id:int,transactions:transaction,db:Session=Depends(get_db)):
    return deposits(db,account_id,transactions.amount)
     

# withdraw
@app.post("/account/withdraw/{account_id}",response_model=transactionout,status_code=status.HTTP_201_CREATED)
def withdraw(account_id:int,transactions:transaction,db:Session=Depends(get_db)):
    return withdraws(db,account_id,transactions.amount)

#transaction history
@app.get("/account/history/{account_id}",response_model=transactionout)
def get_transcation(account_id:int,db:Session=Depends(get_db)):
    return get_transcations(db,account_id)

#transaction all history
@app.get("/account/history_all/",response_model=list[transactionout])
def get_all_transcation(db:Session=Depends(get_db)):
    return get_all_transcations(db)
     

     



   

    