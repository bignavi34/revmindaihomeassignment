from fastapi import APIRouter
from sqlalchemy import text

from app.database import SessionLocal

router = APIRouter()


@router.get("/products")
def get_products():
    db = SessionLocal()

    try:
        query = text("""
            SELECT
                product_name,
                SUM(net_revenue_usd) AS total_net_revenue,
                SUM(units_sold) AS total_units
            FROM sales
            GROUP BY product_name
            ORDER BY total_net_revenue DESC
        """)

        result = db.execute(query)

        return [
            dict(row._mapping)
            for row in result
        ]

    finally:
        db.close()