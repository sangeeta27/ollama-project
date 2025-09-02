# src/main.py

from langchain.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from prompts import prompts

def load_file(file_path: str) -> str:
    """Read file content"""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def run_prompt(llm, prompt_name: str, content: str, question: str = None):
    """Run a prompt template"""
    template = prompts.get(prompt_name)
    if template is None:
        raise ValueError(f"Prompt '{prompt_name}' not found!")

    # Fill in question if needed
    if "{question}" in template and question is not None:
        prompt_text = template.format(content=content, question=question)
    else:
        prompt_text = template.format(content=content)

    # Updated to use 'invoke' instead of direct call
    return llm.invoke(prompt_text)

def main():
    # Initialize Ollama LLM using the updated class
    llm = OllamaLLM(model="llama3")

    # Load file content
    file_content = load_file("example.txt")

    # Example: summary
    summary = run_prompt(llm, "summary", file_content)
    print("Summary:\n", summary)

    # Example: key points
    key_points = run_prompt(llm, "key_points", file_content)
    print("\nKey Points:\n", key_points)

    # Example: Q&A
    question = "What is the main purpose of this file?"
    answer = run_prompt(llm, "questions", file_content, question=question)
    print("\nQ&A:\n", answer)

if __name__ == "__main__":
    main()
