import Link from "next/link";

export default function Navbar() {
  return (
    <nav className="bg-black text-white px-8 py-4 flex justify-between">
      <h1 className="font-bold text-xl">
        NovaBite BI
      </h1>

      <div className="space-x-6">
        <Link href="/">
          Dashboard
        </Link>

        <Link href="/chat">
          Chat
        </Link>
      </div>
    </nav>
  );
}