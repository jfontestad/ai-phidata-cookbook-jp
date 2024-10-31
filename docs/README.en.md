<p align="center">
  <img src="docs/phidata-cookbook-jp.png" width="100%">
  <h1 align="center">🌟 phidata-cookbook-jp 🌟</h1>
</p>
<p align="center">
  <a href="https://github.com/Sunwood-ai-labs/phidata-cookbook-jp">
    <img alt="GitHub Repo" src="https://img.shields.io/badge/github-phidata--cookbook--jp-blue?logo=github">
  </a>
  <a href="https://github.com/Sunwood-ai-labs/phidata-cookbook-jp/blob/main/LICENSE">
    <img alt="License" src="https://img.shields.io/github/license/Sunwood-ai-labs/phidata-cookbook-jp?color=green">
  </a>
  <a href="https://github.com/Sunwood-ai-labs/phidata-cookbook-jp/stargazers">
    <img alt="GitHub stars" src="https://img.shields.io/github/stars/Sunwood-ai-labs/phidata-cookbook-jp?style=social">
  </a>
  <a href="https://github.com/Sunwood-ai-labs/phidata-cookbook-jp/releases">
    <img alt="GitHub release" src="https://img.shields.io/github/v/release/Sunwood-ai-labs/phidata-cookbook-jp?include_prereleases&style=flat-square">
  </a>
  <a href="https://github.com/Sunwood-ai-labs/phidata-cookbook-jp/issues">
    <img alt="GitHub issues" src="https://img.shields.io/github/issues/Sunwood-ai-labs/phidata-cookbook-jp">
  </a>
  <a href="https://github.com/Sunwood-ai-labs/phidata-cookbook-jp/pulls">
    <img alt="PRs Welcome" src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square">
  </a>
  <a href="https://github.com/Sunwood-ai-labs/phidata-cookbook-jp/network/members">
    <img alt="GitHub forks" src="https://img.shields.io/github/forks/Sunwood-ai-labs/phidata-cookbook-jp?style=social">
  </a>
  <a href="https://github.com/Sunwood-ai-labs/phidata-cookbook-jp/watchers">
    <img alt="GitHub watchers" src="https://img.shields.io/github/watchers/Sunwood-ai-labs/phidata-cookbook-jp?style=social">
  </a>
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/Sunwood-ai-labs/phidata-cookbook-jp">
  <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/Sunwood-ai-labs/phidata-cookbook-jp">
</p>
<h2 align="center">
  ～ phidata Cookbook Japanese Explanation Project ～

<a href="https://github.com/Sunwood-ai-labs/phidata-cookbook-jp/blob/main/README.md"><img src="https://img.shields.io/badge/ドキュメント-日本語-white.svg" alt="JA doc"/></a>
<a href="https://github.com/Sunwood-ai-labs/phidata-cookbook-jp/blob/main/docs/README.en.md"><img src="https://img.shields.io/badge/english-document-white.svg" alt="EN doc"></a>
</h2>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai" alt="OpenAI">
  <img src="https://img.shields.io/badge/Gemini-8E75B2?style=for-the-badge&logo=google" alt="Google Gemini">
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git" alt="Git">
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github" alt="GitHub">
  <img src="https://img.shields.io/badge/Actions-2088FF?style=for-the-badge&logo=github-actions" alt="GitHub Actions">
  <img src="https://img.shields.io/badge/YAML-CB171E?style=for-the-badge&logo=yaml" alt="YAML">
  <img src="https://img.shields.io/badge/pip-3775A9?style=for-the-badge&logo=pypi" alt="pip">
  <img src="https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown" alt="Markdown">
  <img src="https://img.shields.io/badge/phidata-FF6B6B?style=for-the-badge" alt="phidata">
</p>

> [!IMPORTANT]
> This repository provides a Japanese explanation and improved organization of the official [phidata](https://github.com/phidatahq/phidata) cookbook. It offers practical sample code and detailed explanations for AI development.

## 🚀 Project Overview

phidata-cookbook-jp is a project that provides detailed explanations in Japanese for the phidata cookbook sample collection.  It focuses particularly on the implementation of AI agents, offering a step-by-step learning structure from basic to advanced concepts. Version: `v1.0.0`

## 🆕 Latest News

- 🎉 **v1.0.0 Release**:  All sample code in the cookbook's `agents` folder has been translated into Japanese, with detailed explanations added.
  - Provides 23 examples of AI agent implementations, ranging from web search to image generation.
  - Detailed Japanese comments have been added to each code snippet.
  - A step-by-step guide for setup and execution has been created.

## ✨ Main Features

1. **Detailed Japanese Explanations**: Detailed comments and explanations have been added to each sample code.
2. **Practical Samples**: Provides 23 examples of AI agent implementations.
3. **Step-by-Step Learning Structure**:  Allows for learning progressively from basic to advanced concepts.
4. **Environment Setup Guide**: Explains how to set up necessary tools and APIs.
5. **Detailed Execution Instructions**:  Provides specific instructions on how to run each sample.

## 📦 Installation Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/phidata-cookbook-jp.git
   cd phidata-cookbook-jp
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate     # Windows
   ```

3. Install dependent packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set environment variables:
   ```bash
   cp .env.example .env
   # Edit the .env file and set the necessary API keys.
   ```

## 🌿 Project Structure

```plaintext
cookbook/
├─ agents/               # Collection of AI agent samples
│  ├─ 01_web_search.py  # Web search agent
│  ├─ 02_finance_agent.py # Financial analysis agent
│  ├─ ...               # Other agent implementations
├─ app.py              # Streamlit application
├─ README.md           # Project description
└─ requirements.txt    # Dependency package list
```

## 📚 Learning Content

The `agents` folder in the cookbook includes examples such as:

1. **Basic Agent Implementations**
   - Web search agent
   - Financial analysis agent
   - Agent team

2. **Advanced Feature Implementations**
   - RAG (Retrieval Augmented Generation)
   - Image generation and analysis
   - Structured data processing

3. **Practical Applications**
   - CLI application
   - Video generation system
   - Data analysis tool

See [agents/README.md](cookbook/agents/README.md) for details.

## 🤝 Contributions

Contributions to this project are welcome:

- Report bugs and suggest features via Issues.
- Improve the code via Pull Requests.
- Suggestions for improving explanations and new sample contributions are also welcome.

## 📄 License

This project is provided under the MIT License.

## 🙏 Acknowledgments

- Thanks to the [phidata](https://github.com/phidatahq/phidata) team for providing excellent implementation examples.
- Thanks to all contributors.

## 🔗 Related Links

- [phidata Official Documentation](https://docs.phidata.com)
- [phidata GitHub](https://github.com/phidatahq/phidata)
- [Community Forum](https://community.phidata.com/)

---

Learn practical AI agent development skills with phidata-cookbook-jp!