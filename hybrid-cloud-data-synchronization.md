## 📄 Runbook 6: Create a file named `hybrid-cloud-data-synchronization.md`

```markdown
# Hybrid Cloud Data Synchronization & Low-Latency Cache Strategy 🔄

This artifact details the data pipeline architecture used to maintain high consistency between legacy on-premise core databases and decoupled cloud-native side-by-side extensions.

---

## 📐 Data Consistency Model

To support real-time data lookups without overwhelming on-premise transactional systems, the platform utilizes an event-driven **Change Data Capture (CDC)** model combined with a high-performance memory cache layer.

On-Premise Core Database ] ➔ [ CDC Agent ] ➔ [ Cloud Event Mesh ] ➔ [ Memory Cache ] ➔ [ Cloud App ]

### 🏎️ Caching & Synchronization Parameters
*   **Cache Invalidation Strategy:** Write-Through / Event-Driven (Any modification at the core source layer publishes a lightweight transaction delta to the event broker to instantly refresh the cloud runtime memory footprint).
*   **Network Latency Protection:** Implements an asymmetric queuing pipeline that guarantees data delivery even during transient site-to-site VPN or network link disruptions.

### 🗺️ Data Sovereignty & Compliance Mapping
| Data Classification | Sync Mechanism | Storage Boundary Rule | Compliance Alignment |
| :--- | :--- | :--- | :--- |
| **Identifiable Core Data** | Tokenized / Masked Event Payload | Retained inside local origin boundaries; never cached on third-party public nodes. | GDPR / Privacy Mandates |
| **Transactional Aggregates** | Asynchronous Micro-Batch Streaming | Stored securely in regional cloud analytical instances. | Corporate Financial Auditing |
| **Static Metadata Configuration** | Scheduled Daily Sync Routine | Distributed globally across regional cache nodes to maximize query speeds. | Core Performance Optimizations |
