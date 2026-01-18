"""Generate examples for the motivation slide.

This code cycles through all prompts in ``prompts.txt``, which contains
prompts of the following form:

(1) Zero-shot inference

(2) Few-shot inference

(3) Chain-of-thought inference
"""

from __future__ import annotations

import pathlib

from cot_pres import utils


def load_prompts() -> dict[str, str]:
    """Load prompts from ``prompts.txt``.
    
    Returns:
        A dictionary of ``{prompt_title: prompt}``.
    """
    currdir = str(pathlib.Path(__file__).parent)
    
    prompts: dict[str, str] = {}
    curr_prompt_name: str | None = None
    curr_prompt: list[str] = []
    
    with open(f"{currdir}/prompts.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            if not line:
                continue

            if line.startswith("prompt: "):
                if curr_prompt_name is not None:
                    prompts[curr_prompt_name] = "\n".join(curr_prompt).rstrip()
                
                curr_prompt_name= line[8:-1]
                curr_prompt = []
                
            else:
                curr_prompt.append(line)
      
        # Process last prompt.          
        assert curr_prompt_name is not None  # for typing. This is guaranteed to not be none.
        prompts[curr_prompt_name] = "\n".join(curr_prompt).rstrip()
        
    return prompts


def main() -> None:
    model = utils.load_model()
    prompts = load_prompts()

    for prompt_type, prompt in prompts.items():
        print(prompt_type)
        output = model(prompt)
    
        print(output[0]["generated_text"])


if __name__ == "__main__":
    main()
