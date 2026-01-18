# Chain-of-Thought Prompting

Contains the source code and all materials used to produce a presentation on chain-of-thought prompting.

This presentation was created as part of DATA 37712 at The University of Chicago.

## Reproducing Results

Each `python` file in `apps` is a standalone module designed to produce output for one slide. All final slides are located in `static`.
To reproduce findings for a particular slide, one need only run the corresponding module, for example:
```{bash}
uv build

uv run python apps/motiv_slide.py
```
