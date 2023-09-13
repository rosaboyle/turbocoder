# Development Vision and Contribution Guidelines

## Project Goal:

The overarching goal of this project is to augment the developer experience by automating the mundane aspects of coding, thereby allowing developers to concentrate on more creative, fulfilling tasks and solving real-world problems. Through leveraging Language Models (LLMs), the project aims to generate ready-to-use, well-tested, and thoroughly documented code just from a prompt. 

## Guidelines:

### Acknowledge LLM Limitations

- **LLMs Are Tools, Not Replacements**: While LLMs, including ChatGPT, bring impressive capabilities, they are not infallible—especially when it comes to generating system-level code. This project aims to serve as a supplementary tool to assist developers rather than replace their expertise.

### Consistency with Existing Practices

- **Respect Community Conventions**: Do not reinvent the wheel by changing frameworks or altering development workflows that have stood the test of time. Our aim should not be to disrupt but to integrate seamlessly. For instance, we should respect the directory structures commonly used in projects and aim to generate code that would be indistinguishable from what a skilled human developer would produce.

### Interpretability First

- **Transparency Over Optimization**: As we aim to serve developers by taking their prompts and delivering ready-to-go code, interpretability in each step of the process is vital. From the way prompts are understood to how code is generated, tested, and documented, every phase should be clear and easily comprehensible by the end-user.

  - **Descriptive Approach**: ChatGPT should ideally follow a sequence of Describing the problem, Analyzing it, Coding a solution, Testing the solution, Iterating upon it, and then Improving it. This offers users a comprehensible logic flow that they can follow and learn from.
  
  - **Experimental Branch for Optimizations**: While optimizations are crucial, they should not come at the expense of interpretability. Any attempt to streamline or fuse multiple steps should be initially placed in an experimental branch for evaluation and should not affect the main product until thoroughly vetted.

### Contributions

- **Open for Collaboration**: We welcome contributions that align with the vision and guidelines outlined here. It’s not just about code; documentation, testing, and even discussions are valuable contributions.
  
- **Peer Reviews**: Every significant change should be peer-reviewed. This not only ensures the quality of the code but also aligns everyone’s understanding and keeps the codebase maintainable.

By adhering to these guidelines, we aspire to create a tool that adds substantial value to the development process, alleviating the tedium of repetitive tasks and enabling developers to focus on what truly matters: solving problems and innovating.
