"use client";

import {
  useEffect,
  useState,
} from "react";

import api from "@/lib/api";
import KPICard from "@/components/KPICard";
import RevenueChart from "@/components/RevenueChart";

export default function Dashboard() {
  const [summary, setSummary] =
    useState<any>(null);

  const [trends, setTrends] =
    useState<any[]>([]);

  useEffect(() => {
    loadData();
  }, []);

  async function loadData() {
    const summaryRes =
      await api.get(
        "/api/summary"
      );

    const trendsRes =
      await api.get(
        "/api/trends"
      );

    setSummary(
      summaryRes.data
    );

    setTrends(
      trendsRes.data
    );
  }

  if (!summary)
    return (
      <div className="p-10">
        Loading...
      </div>
    );

  return (
    <main className="p-10">
      <h1 className="text-4xl font-bold mb-8">
        NovaBite Dashboard
      </h1>

      <div className="grid md:grid-cols-3 gap-6 mb-10">
        <KPICard
          title="Total Revenue"
          value={`$${summary.total_net_revenue}`}
        />

        <KPICard
          title="Gross Margin"
          value={`${summary.gross_profit_margin}%`}
        />

        <KPICard
          title="Top Region"
          value={summary.top_region}
        />
      </div>

      <RevenueChart
        data={trends}
      />
    </main>
  );
}