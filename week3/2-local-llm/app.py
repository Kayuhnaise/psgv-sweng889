import os
import time
import requests


OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")


def wait_for_ollama():
    print("Waiting for Ollama to start...")

    for _ in range(30):
        try:
            response = requests.get(f"{OLLAMA_URL}/api/tags")
            if response.status_code == 200:
                print("Ollama is running.")
                return
        except requests.exceptions.ConnectionError:
            pass

        time.sleep(2)

    raise RuntimeError("Ollama did not start in time.")


def pull_model():
    print(f"Pulling model: {MODEL}")

    response = requests.post(
        f"{OLLAMA_URL}/api/pull",
        json={"model": MODEL},
        stream=True,
    )

    if response.status_code != 200:
        raise RuntimeError(f"Failed to pull model: {response.text}")

    for line in response.iter_lines():
        if line:
            print(line.decode("utf-8"))

    print("Model is ready.")


def ask_model(prompt):
    response = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
        },
    )

    if response.status_code != 200:
        raise RuntimeError(f"Failed to generate response: {response.text}")

    return response.json()["response"]


def main():
    wait_for_ollama()
    pull_model()

    prompt = "Explain Docker in one short paragraph for a beginner."
    answer = ask_model(prompt)

    print("\nPrompt:")
    print(prompt)

    print("\nLLM response:")
    print(answer)


if __name__ == "__main__":
    main()
