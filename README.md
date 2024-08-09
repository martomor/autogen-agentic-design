# AI Agentic Design Patterns with AutoGen


This repository contains my notes and code for the [AI Agentic Design Patterns with AutoGen](https://www.deeplearning.ai/short-courses/ai-agentic-design-patterns-with-autogen/) offered by DeepLearning AI.

## Main Topics Covered

- Multi-agent Collaboration
- Reflection
- Code Generation
- Planning


## AutoGen Summary

AutoGen is a framework for developing LLM applications with multiple customizable agents that converse to solve tasks, integrating human input seamlessly.

**Main Features:**

1. Multi-Agent Conversations: Facilitates building advanced LLM applications with minimal effort.
2. Workflow Optimization: Streamlines orchestration and automation of complex LLM workflows.
3. Performance Enhancement: Boosts LLM models' performance and addresses weaknesses.
4. Diverse Patterns: Supports various conversation patterns and configurations.
5. Application Range: Demonstrates versatility across multiple domains with systems of varying complexities.

![Autogen](assets/Autogen.png)

## How to use this repo

To get started, please follow the instructions below:

1. Clone the repository to your local machine:
```
git clone https://github.com/your-username/autogen-agentic-design.git
```

2. Install Python 3.11.9 on your system. You can use either pyenv or conda to manage your Python versions. Here are the steps for each option:

    - Using pyenv:
      - Install pyenv by following the instructions [here](https://github.com/pyenv/pyenv#installation).
      - Once pyenv is installed, run the following command to install Python 3.11.9:
         ```
         pyenv install 3.11.9
         ```
      - Set Python 3.11.9 as the global version by running:
         ```
         pyenv global 3.11.9
         ```

    - Using conda:
      - Install conda by following the instructions [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).
      - Create a new conda environment with Python 3.11.9 by running:
         ```
         conda create -n autogen python=3.11.9
         ```
      - Activate the environment by running:
         ```
         conda activate autogen
         ```

3. Install the required dependencies using either pip or Poetry. Here are the steps for each option:

    - Using pip:
      - Navigate to the project directory:
         ```
         cd autogen-agentic-design
         ```
      - Install the dependencies:
         ```
         pip install -r requirements.txt
         ```

    - Using Poetry:
      - Navigate to the project directory:
         ```
         cd autogen-agentic-design
         ```
      - Install Poetry by following the instructions [here](https://python-poetry.org/docs/#installation).
      - Install the dependencies:
         ```
         poetry install
         ```


