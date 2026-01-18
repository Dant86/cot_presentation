"""Few-shot examples with GPT."""

from __future__ import annotations

import transformers


def main() -> None:
    pipeline = transformers.pipeline(
        task="text-generation", model="openai-community/gpt2"
    )

    output = pipeline(
        "Alice has two apples and Bob has three apples. If Bob gives Alice half his apples, how many does Alice have?"
    )
    
    print(output[0]["generated_text"])


if __name__ == "__main__":
    main()
