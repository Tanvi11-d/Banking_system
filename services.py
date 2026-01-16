from models import Transaction,Account,create_table
from database import *
from sqlalchemy.orm import Session
from schema import accountcreate,accountupdate
from fastapi import HTTPException
from main import *
from logger import logger

create_table()

# create account
def create_accounts(db:Session,account:accountcreate):
    try:
        account = Account(name=account.name,email=account.email,age=account.age,city=account.city,balance=account.balance)
        db.add(account)
        db.commit() 
        db.refresh(account)
        logger.info(f'account created :{account.email}')
        return account
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=404,detail="account creation failed")

# fetch records
def get_accounts(db:Session,account_id):
    account=db.query(Account).filter(Account.id==account_id).first()
    if account is None:
                raise HTTPException(status_code=404,detail="account not found!")
    return account
 
      

# fetch all records
def get_all_accounts(db:Session):
    accounts=db.query(Account).all()
    if accounts is None:
                raise HTTPException(status_code=404,detail="account not found!")
    return accounts

# update account
def update_accounts(db:Session,account_id,accounts:accountupdate):
    try:
        db_account=db.query(Account).filter(Account.id==account_id).first()
        
        db_account.name=accounts.name
        db_account.email=accounts.email
        db_account.age=accounts.age
        db_account.city=accounts.city

        db.commit()
        db.refresh(db_account)
        logger.info('account updated')
        return db_account
    except:
        if db_account is None:
            raise HTTPException(status_code=404,detail=f"account not found!")


# delete account
def delete_accounts(db:Session,account_id:int):
    db_account=get_accounts(db,account_id)
    db.delete(db_account)
    db.commit()

    return db_account

# Deposit
def deposits(db:Session,account_id:int,amount:float):
    try:
        account=get_accounts(db,account_id)
        print("account.balanc:", account.balance)
        print("transactions.amount:",amount)
        account.balance+=amount

        tsn=Transaction(account_id=account_id,type="deposit",amount=amount)
        db.add(tsn)
        db.commit()
        db.refresh(tsn)
        logger.info("transaction completed")
        return tsn
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=404,detail="deposite failed")
    

# withdraw
def withdraws(db:Session,account_id:int,amount:float):
    try:
        account=get_accounts(db,account_id)
        if account.balance < amount:
            raise HTTPException(status_code=404,detail="balance not inefficient")

        account.balance-=amount
        txn=Transaction(account_id=account_id,type="withdraw",amount=amount)
        db.add(txn)
        db.commit()
        db.refresh(txn)
        logger.info("transaction completed")
        return txn

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=404,detail="withdraw failed")


# transaction history
def get_transcations(db:Session,account_id):
    trans_hist=db.query(Transaction).filter(Transaction.id==account_id).first()
    if trans_hist is None:
        raise HTTPException(status_code=404,detail="Transcation not found!")
    return trans_hist

# transaction all history
def get_all_transcations(db:Session):
    transaction=db.query(Transaction).all()
    if transaction is None:
        raise HTTPException(status_code=404,detail="transcation not found!")
    return transaction