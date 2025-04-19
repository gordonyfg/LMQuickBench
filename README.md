# LMQuickBench

A lightweight, flexible CLI tool for benchmarking local LLMs running on LM Studio.  
Easily measure response latency, token usage, and generation speed.

---

## ✨ Features

- Benchmark LLM models locally via LM Studio's inference server
- Measure latency, token count, and tokens per second
- Flexible server URL (support localhost, LAN, custom port)
- Single prompt or batch prompts
- Simple CLI usage
- Ready for expansion (CSV output, Streamlit dashboard, etc.)

---

## 📦 Installation

First, clone the repository:

```bash
git clone https://github.com/yourusername/LMQuickBench.git
cd LMQuickBench
```

Then install locally:

```bash
pip install -e .
```

✅ After install, the `lmquickbench` command is available globally.

---

## 🚀 Quick Start

Make sure your LM Studio Inference Server is running!

Example: Run a quick benchmark on the default LM Studio server (localhost:1234):

```bash
lmquickbench --prompt "What is Artificial Intelligence?"
```

Example: Use a custom server URL:

```bash
lmquickbench --prompt "Explain recursion." --server_url "http://192.168.1.100:5678/v1/chat/completions"
```

Example: Run a batch of prompts:

```bash
lmquickbench --promptfile prompts/prompts_coding.txt --max_tokens 512
```

---

## ⚙️ CLI Options

| Option | Description | Default |
|:---|:---|:---|
| `--prompt` | A single prompt to test | |
| `--promptfile` | A text file containing prompts (1 per line) | |
| `--server_url` | LM Studio server endpoint URL | `http://localhost:1234/v1/chat/completions` |
| `--max_tokens` | Maximum tokens for model output | 512 |

---

## 📊 Example Output

```
Testing prompt: What is AI?
Model: qwen2.5-coder-14b-instruct, Latency: 4.56 sec, Tokens: 133, Tokens/sec: 29.14
Output: AI stands for Artificial Intelligence...
```

---

## 🧪 Development

To install development requirements:

```bash
pip install -r requirements.txt
```

Run unit tests:

```bash
pytest
```

---

## 📈 CI/CD

LMQuickBench uses GitHub Actions for automatic testing on push and PRs.  
See `.github/workflows/ci.yml` for workflow details.

---

## 🛣️ Roadmap

- CSV/JSON result output
- System resource (CPU/RAM) monitoring
- Streamlit dashboard visualization
- PyPI release
- Optional Homebrew installer

---

## 🧑‍💻 Author

Created by Gordon Yeung.  
[GitHub Profile](https://github.com/yourusername)

---

## 📄 License

MIT License