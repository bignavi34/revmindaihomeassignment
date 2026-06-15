from fastapi import APIRouter
from sqlalchemy import text

from app.database import SessionLocal

router = APIRouter()


@router.get("/summary")
def get_summary():
    db = SessionLocal()

    try:
        total_query = text("""
            SELECT
                SUM(net_revenue_usd) AS total_revenue,
                SUM(units_sold) AS total_units,
                SUM(gross_profit_usd) AS total_profit
            FROM sales
        """)

        totals = db.execute(total_query).fetchone()

        total_revenue = totals.total_revenue
        total_units = totals.total_units
        total_profit = totals.total_profit

        gross_margin = (
            total_profit / total_revenue * 100
            if total_revenue
            else 0
        )

        top_region = db.execute(text("""
            SELECT region
            FROM sales
            GROUP BY region
            ORDER BY SUM(net_revenue_usd) DESC
            LIMIT 1
        """)).scalar()

        top_channel = db.execute(text("""
            SELECT channel
            FROM sales
            GROUP BY channel
            ORDER BY SUM(net_revenue_usd) DESC
            LIMIT 1
        """)).scalar()

        top_product = db.execute(text("""
            SELECT product_name
            FROM sales
            GROUP BY product_name
            ORDER BY SUM(net_revenue_usd) DESC
            LIMIT 1
        """)).scalar()

        return {
            "total_net_revenue": round(total_revenue, 2),
            "total_units": total_units,
            "gross_profit_margin": round(
                gross_margin,
                2,
            ),
            "top_region": top_region,
            "top_channel": top_channel,
            "top_product": top_product,
        }

    finally:
        db.close()