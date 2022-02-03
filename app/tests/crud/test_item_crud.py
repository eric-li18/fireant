from sqlalchemy.orm import Session
from app.crud import pokemon
from app.schemas import BugCreate
from app.tests.utils import utils


def test_create_item(db: Session):
    itemname = utils.random_string()
    price = utils.random_float()
    item_model = BugCreate(itemname=itemname, price=price)
    created_mon = pokemon.create(db, item_model)
    assert created_mon.itemname == itemname
    assert created_mon.price == price
