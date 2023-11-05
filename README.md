# LLM OS

The idea is to explore LLMs as the kernel process of an OS,
inspired by [Karpathy](https://x.com/karpathy/status/1707437820045062561?s=20)
as part of [Backdrop Build](https://backdropbuild.com/).

LLM vs OS:

- I/O: Multimodal input and output after vectorizing/tokenizing
- IPC / Networking: Plugins to handle internet APIs and browser access
- CPU / Runtime exec / Scheduler: Eval of code in any prog. language (sandboxed), at any time. Smarter scheduler.
- File System: Plugins to handle local FS
- Physical/Virtual Memory: Vector based memory (memGPT)

New possibilities to explore:

- Non-deterministic / flexibility
- AutoGPT-ish mechanism to extend it's own implementation

What the v0 could be?

- Put all those pieces together and solve a toy problem

# Refs

- https://github.com/cpacker/MemGPT
- https://github.com/stanfordnlp/dspy
- https://github.com/langchain-ai/langchain
