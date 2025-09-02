# Ollama + LangChain Mini Project

This project demonstrates:

- Running a **local Llama 3.x model** with Ollama
- Using **LangChain** PromptTemplates
- Configurable prompts for **summary, key points, and Q&A**
- Basic Pytest integration



## Setup

1. **Clone the repository**:
```bash
git clone <your-repo-url>
cd ollama_project

2. Create and activate Python virtual environment:
python -m venv venv
# Activate the environment
# On macOS/Linux:
source venv/bin/activate
# On Windows (PowerShell):
venv\Scripts\Activate.ps1

3. Install dependencies:

pip install -r requirements.txt
# Or install individually:
pip install langchain ruff pytest langchain-ollama

4. Pull Llama 3.x model using Ollama:
ollama pull llama3

Run the Project

With the virtual environment activated:

python src/main.py

