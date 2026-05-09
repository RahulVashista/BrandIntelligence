export default function App() {
  const sections = [
    "Dashboard","Investigations","Monitoring","Alerts","IOC Explorer","Infrastructure Graph","Brand Management","🔑 API Keys","Settings","Hacker View"
  ]

  return (
    <div style={{ display: "flex", minHeight: "100vh", background: "#0d1117", color: "#e6edf3", fontFamily: "Inter, sans-serif" }}>
      <aside style={{ width: 260, borderRight: "1px solid #30363d", padding: 16 }}>
        <h2>BrandIntelligence</h2>
        {sections.map((s) => <div key={s} style={{ padding: "8px 0" }}>{s}</div>)}
      </aside>
      <main style={{ padding: 24 }}>
        <h1>Analyst Dashboard</h1>
        <p>Live scan queue, phishing trends, risk distribution, and infrastructure clustering.</p>
      </main>
    </div>
  )
}
