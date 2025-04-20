# LMQuickBench

[![PyPI version](https://badge.fury.io/py/lmquickbench.svg)](https://badge.fury.io/py/lmquickbench)
[![CI](https://github.com/gordonyfg/LMQuickBench/actions/workflows/ci.yml/badge.svg)](https://github.com/gordonyfg/LMQuickBench/actions/workflows/ci.yml)

A lightweight, flexible CLI tool for benchmarking local LLM models running through [LM Studio](https://lmstudio.ai/).  
Measure latency, token usage, and output speed easily from your terminal.

---

## ✨ Features

- 📝 Single or batch prompt testing
- 🔗 Dynamic server URL connection (localhost, LAN, docker, etc.)
- ⏱️ Measure latency, tokens, tokens/sec
- ⚡ Fast, simple, no heavy dependencies
- 🚀 Pip-installable: easy to set up and use
- 🛠️ Expandable design (CSV export, dashboard, future extensions)

---

## 📦 Installation

Install LMQuickBench directly from PyPI:

```bash
pip install lmquickbench
```

Or install locally from source:

```bash
git clone https://github.com/gordonyfg/LMQuickBench.git
cd LMQuickBench
pip install -e .
```

---

## 🚀 Quick Start

Make sure your LM Studio inference server is running!

Run a quick benchmark:

```bash
lmquickbench --prompt "Explain recursion." --max_tokens 512
```

Use a custom server URL:

```bash
lmquickbench --prompt "Summarize AI history." --server_url "http://192.168.1.100:5678/v1/chat/completions"
```

Run a batch benchmark using a prompts file:

```bash
lmquickbench --promptfile prompts/prompts_coding.txt --max_tokens 512
```

---

## ⚙️ CLI Options

| Option | Description | Default |
|:---|:---|:---|
| `--prompt` | A single prompt to benchmark | |
| `--promptfile` | A text file with multiple prompts (one per line) | |
| `--server_url` | URL of the LLM server endpoint | `http://localhost:1234/v1/chat/completions` |
| `--max_tokens` | Maximum output tokens to generate | 512 |

---

## 📊 Example Output

```
Testing prompt: Explain recursion.
Model: qwen2.5-coder-14b-instruct, Latency: 4.56 sec, Tokens: 133, Tokens/sec: 29.14
Output: Recursion is a method where the solution to a problem depends on solutions to smaller instances of the same problem...
```

---

## 🛡️ Development & Contribution

Clone the repo:

```bash
git clone https://github.com/gordonyfg/LMQuickBench.git
cd LMQuickBench
```

Install development dependencies:

```bash
pip install -r requirements.txt
```

Run tests locally:

```bash
pytest -v
```

We welcome contributions! Feel free to open issues, suggest improvements, or submit pull requests.

---

## 📈 Continuous Integration

- GitHub Actions automatically run all tests on every push and PR.
- See the [Actions tab](https://github.com/gordonyfg/LMQuickBench/actions) for CI status.

---

## 🛣️ Roadmap

- [ ] CSV/JSON export of benchmark results
- [ ] Streamlit web dashboard visualization
- [ ] System resource monitoring (CPU/RAM usage)
- [ ] Integration with other LLM inference servers (e.g., Ollama, llama.cpp)

---

## 📜 License

This project is licensed under the MIT License.

---

## 🧑‍💻 Author

Created and maintained by [Gordon Yeung](https://github.com/gordonyfg).

---

## 🌍 Links

- [PyPI: lmquickbench](https://pypi.org/project/lmquickbench/)
- [GitHub Repository](https://github.com/gordonyfg/LMQuickBench)
- [LM Studio Website](https://lmstudio.ai/)