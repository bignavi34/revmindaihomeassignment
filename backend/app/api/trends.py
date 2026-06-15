from fastapi import APIRouter
from sqlalchemy import text

from app.database import SessionLocal

router = APIRouter()


@router.get("/trends")
def get_trends():
    db = SessionLocal()

    try:
        query = text("""
            SELECT
                month,
                SUM(net_revenue_usd) AS revenue
            FROM sales
            GROUP BY month
            ORDER BY month
        """)

        result = db.execute(query)

        return [
            {
                "month": row.month,
                "revenue": round(row.revenue, 2)
            }
            for row in result
        ]

    finally:
        db.close()