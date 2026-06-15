from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Float

from app.database import Base


class Sale(Base):
    __tablename__ = "sales"

    transaction_id = Column(String, primary_key=True)

    date = Column(String)
    month = Column(String)
    quarter = Column(String)

    sku = Column(String)
    product_name = Column(String)
    category = Column(String)
    subcategory = Column(String)

    region = Column(String)
    channel = Column(String)
    sales_rep = Column(String)

    units_sold = Column(Integer)

    unit_price_usd = Column(Float)
    gross_revenue_usd = Column(Float)
    discount_pct = Column(Float)
    net_revenue_usd = Column(Float)
    cogs_usd = Column(Float)
    gross_profit_usd = Column(Float)