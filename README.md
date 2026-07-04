# Qwythos — The Uncensored Mythos-Class Desktop Studio

[![Latest Release](https://img.shields.io/github/v/release/qwythos-mythos/qwythos?style=flat-square&label=Download)](https://github.com/qwythos-mythos/qwythos/releases/latest)
[![Windows](https://img.shields.io/badge/Windows-10%20%7C%2011-blue?style=flat-square)](https://github.com/qwythos-mythos/qwythos/releases/latest)
[![macOS](https://img.shields.io/badge/macOS-Apple%20Silicon%20%7C%20Intel-black?style=flat-square)](https://github.com/qwythos-mythos/qwythos/releases/latest)
[![Model](https://img.shields.io/badge/Engine-Qwythos--9B-D97757?style=flat-square)](https://huggingface.co/empero-ai)
[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)

Anthropic locked the Claude Mythos intelligence behind government contracts and crippled Fable 5 with extreme censorship. **Qwythos Desktop** brings that frontier-level reasoning to your local machine. This is an entirely uncensored, 1-million-token context, 9B-parameter AI engine packaged as a native desktop client for Windows and Mac. Drop in zero-day exploits, analyze EDR bypasses, and reverse-engineer malware locally—without API restrictions, content filters, or vendor surveillance.

Distilled from over 500 million tokens of high-quality Claude Mythos and Fable traces using an assistant-only loss function, the underlying **Qwythos-9B** architecture achieves a massive **+34.3 MMLU uplift** over its base. Processed through the Heretic abliteration pipeline (achieving a microscopic KL divergence of 0.0066), the model is permanently stripped of corporate safety classifiers. You get the elite analytical power of Anthropic's top tier, executing locally on your own hardware.

---

## 💻 Hybrid Burst Inference: Frontier AI on an RTX 3060

The biggest barrier to open-source AI is hardware. You shouldn't need a $40,000 server rack to run top-tier reasoning. **Qwythos Desktop** introduces a revolutionary **Hybrid Burst** architecture designed to democratize massive context windows.

Thanks to advanced GGUF Q4_K_M quantization and MLX framework integration, the core model weighs just 5.6 GB. This means the entire intelligence engine—including its dense `<think>` reasoning paths and native tool-calling capabilities—fits effortlessly inside the 12GB VRAM of a standard consumer **NVIDIA RTX 3060** or a base model Apple M1 Mac. 

When your workload is standard (chat, scripting, local file analysis), 100% of the computation happens on your local GPU. However, loading a **1M token context** (like an entire enterprise repository or hundreds of PCAP logs) requires immense memory for the KV-cache. Instead of crashing out of memory (OOM), Qwythos Desktop seamlessly triggers **Hybrid Burst Mode**. The client dynamically offloads the heavy KV-cache processing to your configured API (Bring-Your-Own-Key or a compatible backend endpoint), while keeping the core reasoning loop local. You get local privacy for standard tasks, and infinite cloud-backed memory when you need to swallow an entire codebase whole.

---

## 🛡️ The End of Mandatory Data Retention

Using cloud models for InfoSec is inherently compromised. Anthropic enforces a strict, un-opt-outable 30-day data retention policy for its Claude Fable 5 commercial deployments. Feeding sensitive corporate infrastructure logs, proprietary code, or unpatched vulnerabilities into a cloud API effectively leaks your zero-days to a third-party vendor. 

**Qwythos Desktop** operates on a **Zero-Trust** paradigm. 
By pulling the model out of the cloud and into a native executable, we sever the telemetry loop. The application analyzes offensive payloads, ransomware kill-chains, and TLS handshake structures entirely on your hard drive. There is no middleman, no "Trust and Safety" monitoring daemon, and no API gateway scanning your prompts. Your threat intelligence remains completely air-gapped. 

---

## ⚙️ Core Desktop Capabilities

**Deeply Uncensored Cybersec:**
Unlike "aligned" models that generate generic disclaimers when asked for technical depth, the abliterated Qwythos engine delivers. Get actionable, defender-oriented breakdowns of SQL injections, process-injection evasion techniques, and MITRE ATT&CK ransomware paths without the AI lecturing you on ethics.

**1M YaRN Hyper-Context:**
The desktop client leverages YaRN (Yet another RoPE extensioN) with a 4.0 scaling factor integrated directly into the config. Drop 500,000 lines of code into the workspace; the Gated DeltaNet linear attention processes it with sub-quadratic memory scaling, maintaining pinpoint accuracy across dozens of interconnected files.

**Native Mythos Reasoning (CoT):**
We didn't just wrap a prompt around a basic model. Qwythos-9B uses synthetic Chain-of-Thought (CoT) generated via the proprietary *rethink* tool. Before answering, the model opens a `<think>` block to formulate hypotheses and test variants, mirroring the elite analytical pacing of Claude Mythos. 

**Autonomous Agency (Tool Calling):**
Qwythos natively speaks XML function calling (`<tool_call>`). Give the desktop client access to its sandboxed terminal or Python executor, and it will independently search hashcat modes, execute Nmap scans, or query medical pharmacology databases, self-correcting its trajectory in real-time.

---

## 📊 Competitive Positioning

| Capability | Qwythos Desktop | Claude Fable 5 | Claude Opus 4.8 | Qwable-9B |
|---|---|---|---|---|
| **Uncensored Cybersec** | **Yes (Heretic Abliterated)** | No (Auto-routes to safe model) | No (Strict guardrails) | No (Inherited Fable censorship) |
| **Local Execution** | **Yes (RTX 3060 / Mac native)** | No (Cloud only) | No (Cloud only) | CLI only |
| **Context Window** | **1,048,576 Tokens** | 1,000,000 Tokens | 200,000 Tokens | 262,144 Tokens |
| **Data Privacy** | **Zero Data Retention** | 30-Day Mandatory Logging | Standard Logging | Open Source / CLI |
| **Cost Profile** | **Free / Bring Your Own Compute** | $15.00 / 1M Tokens | $15.00 / 1M Tokens | Free (Weaker capabilities) |

*(Note: Qwable-9B is an alternative open distillation trained purely on public traces. It retains corporate censorship and fails on advanced DevOps and InfoSec reasoning compared to Qwythos' proprietary Mythos-trace dataset).*

---

## 📥 Installation

Forget Python environments, Hugging Face tokens, and compiling custom CUDA kernels. Qwythos Desktop is packaged as a standalone application with the inference engine bundled inside.

*   **Windows:** Download `Qwythos-x64.7z` from the latest release. Run the installer. 
*   **macOS:** Download `Qwythos.dmg` from the latest release. Drag to Applications. (Universal Binary for Apple Silicon and Intel).

Double-click to launch. The app automatically detects your hardware, selects the optimal quantization profile, and starts the local engine.

---

## ❓ Frequently Asked Questions

**1. How is this completely free to use?**
The underlying Qwythos-9B model is distributed under the permissive Apache 2.0 license by Empero AI. We provide the native desktop wrapper, GUI, and local inference engine (via bundled llama.cpp/MLX) as a completely free, MIT-licensed open-source project. You only pay for electricity, or external API costs if you choose to use the Hybrid Burst offload feature.

**2. What happens when my RTX 3060 chokes on a massive 1M-token codebase?**
Your VRAM handles the model weights easily (5.6GB for Q4_K_M). When you paste a massive document that balloons the KV-cache beyond your remaining VRAM, Qwythos Desktop seamlessly shifts to Hybrid Burst mode. It offloads the context cache to your designated API endpoint, preserving the interface speed without crashing your system.

**3. Is it safe to give an intentionally uncensored AI access to my local terminal?**
The Qwythos application runs external tool executions within a restricted local sandbox. However, because the model's safety constraints have been completely abliterated, it *will* write destructive code if you explicitly ask it to. You are using a professional Red Teaming tool; you assume full responsibility for the payloads you execute on your host machine.

**4. Why should I use this over the Qwable-9B distillation?**
Qwable-9B was trained strictly on a limited public dataset of early Fable 5 traces. It inherited Anthropic's corporate politeness, sterile refusal mechanisms, and struggles with complex DevOps/Cybersec edge cases. Qwythos-9B was trained on 500M+ tokens of elite, internal Mythos traces and surgically stripped of censorship, making it fundamentally superior for technical research.

**5. How does the 1M YaRN hyper-context actually work in practice?**
Instead of using standard attention which breaks down over long distances, the model utilizes Gated DeltaNet linear attention combined with a YaRN (Yet another RoPE extensioN) scaling factor of 4.0. In practice, this means you can drag and drop 15 different PDF whitepapers, a 50,000-line server log, and a Python repository into the chat, and the model will reference an exact variable on page 400 without hallucinating.

---

## 🔒 Privacy & Security Model

*   **Zero Telemetry:** The application contains absolutely no analytics trackers, crash reporters, or usage beacons.
*   **Air-Gapped Operation:** The core inference engine requires zero internet connection to function once the weights are downloaded.
*   **Local Storage Only:** All prompts, workspaces, and chat histories are encrypted and stored solely on your local storage drive.
*   **Auditable Sandboxing:** The native tool-execution environment is isolated; you must explicitly grant the client permission to read or write to directories outside the project folder.
*   **No Vendor Lock-in:** Open weights, open source client. Anthropic cannot revoke your access via an API ban.

---

## 🗺️ Roadmap

*   **v1.2** — Full Multi-Token Prediction (MTP) layer support for 2x generation speed.
*   **v1.3** — Peer-to-peer swarm KV-cache offloading (combine VRAM with local network machines).
*   **v2.0** — Background IDE extension hooks (VS Code / JetBrains) utilizing the local engine.

## Disclaimer

This is an independent open-source desktop client built to run the Empero AI Qwythos-9B model. It is not affiliated with, endorsed by, or sponsored by Anthropic, Alibaba, or Empero AI. "Claude," "Mythos," and "Fable" are trademarks of Anthropic. Their use in this repository is strictly for comparative and nominative fair use purposes to describe the training lineage and capability targets of the open-weight model. Qwythos Desktop relies entirely on local execution unless configured otherwise by the user. Ensure your use of uncensored AI complies with local regulations regarding cybersecurity and malware analysis.
