from sqlalchemy import text


def get_context(question: str, db):
    q = question.lower()

    if "highest net revenue" in q and "q1 2024" in q:
        result = db.execute(
            text("""
                SELECT
                    region,
                    SUM(net_revenue_usd)
                    AS revenue
                FROM sales
                WHERE quarter='Q1-2024'
                GROUP BY region
                ORDER BY revenue DESC
                LIMIT 1
            """)
        )

        row = result.fetchone()

        if row:
            return {
                "region": row.region,
                "revenue": row.revenue
            }

    return {
        "message":
        "Could not determine query."
    }
