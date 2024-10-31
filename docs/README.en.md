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
> This repository provides a Japanese explanation and reorganized version of the official [phidata](https://github.com/phidatahq/phidata) cookbook. It offers practical sample code and detailed explanations for AI development.

## 🚀 Project Overview

phidata-cookbook-jp is a project that provides detailed explanations in Japanese for the phidata cookbook sample collection.  It focuses particularly on the implementation of AI agents, offering a step-by-step learning structure from basic to advanced concepts. Version: `v0.1.0`

## 🆕 Latest News

- **v0.1.0 Release**: All sample codes in the `agents` folder of the official phidata cookbook have been translated into Japanese with detailed explanations added.  It provides 23 AI agent implementation examples and a step-by-step guide from setup to execution. The English README has also been updated. The repository name has also been changed. Many new features and improvements have been added.


## ✨ Main Features

- Detailed Japanese explanations: Detailed comments and explanations have been added to each sample code.
- Practical samples: 23 different AI agent implementation examples are provided.
- Step-by-step learning structure:  Learn sequentially from basic to advanced concepts.
- Environment setup guide: Explains how to set up the necessary tools and APIs.
- Detailed execution instructions:  Specifically explains how to run each sample.


## 📦 Installation Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Sunwood-ai-labs/phidata-cookbook-jp.git
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

4. Set environment variables: Copy `.env.example` to `.env` and set the necessary API keys, etc.


## 🌿 Project Structure

cookbook/
├─ agents/               # Collection of AI agent samples
│  ├─ 01_web_search.py  # Web search agent
│  ├─ 02_finance_agent.py # Financial analysis agent
│  ├─ ...               # Other agent implementations (23 in total)
├─ app.py              # Streamlit application
├─ requirements.txt    # Dependency package list


## 📚 Learning Content

The `cookbook/agents` folder contains various AI agent implementation examples. Agents are provided for various tasks, including web search, financial analysis, image generation, and video generation.  See the comments in each file and `cookbook/agents/README.md` for details.


## 🤝 Contributions

Contributions to this project are welcome. We welcome various contributions such as bug reports, feature suggestions, code improvements, explanation improvements, and suggestions for new samples via GitHub Issues and Pull Requests.


## 📄 License

This project is provided under the MIT License.


## 🙏 Acknowledgements

- iris-s-coon
- Maki 

## 🔗 Reference Links

- [phidata Official Documentation](https://docs.phidata.com)
- [phidata GitHub](https://github.com/phidatahq/phidata)
- [Community Forum](https://community.phidata.com/)

---

Learn practical AI agent development skills with phidata-cookbook-jp!