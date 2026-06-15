"use client";

import { useState } from "react";
import api from "@/lib/api";

export default function ChatPage() {
  const [question, setQuestion] =
    useState("");

  const [answer, setAnswer] =
    useState("");

  const [loading, setLoading] =
    useState(false);

  async function askQuestion() {
    if (!question) return;

    setLoading(true);

    try {
      const res =
        await api.post(
          "/api/chat",
          {
            question,
          }
        );

      setAnswer(
        res.data.answer
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="p-10 max-w-4xl mx-auto">
      <h1 className="text-4xl font-bold mb-8">
        NovaBite AI Chat
      </h1>

      <textarea
        rows={4}
        className="w-full border rounded-lg p-4"
        value={question}
        onChange={(e) =>
          setQuestion(
            e.target.value
          )
        }
      />

      <button
        onClick={askQuestion}
        className="bg-black text-white px-6 py-3 rounded-lg mt-4"
      >
        Ask
      </button>

      {loading && (
        <p className="mt-4">
          Thinking...
        </p>
      )}

      {answer && (
        <div className="mt-8 border rounded-lg p-6">
          {answer}
        </div>
      )}
    </main>
  );
}