# Project Context for PocketFlow Development 🌊

## Introduction
This project is built using the **PocketFlow** framework, a minimalist library designed for building modular and agentic workflows. It emphasizes clear abstractions for creating composable and scalable LLM applications.

---

## PocketFlow Core Abstractions 🧩

### 1. Nodes
* **Definition**: A `Node` is the fundamental, atomic unit of computation in PocketFlow. It encapsulates a single, well-defined task or operation.
* **Purpose**: Nodes are designed to be reusable and independent, making workflows easy to reason about and test.
* **Structure**:
    * All Node classes **must inherit** from `pocketflow.Node`.
    * They typically implement lifecycle methods for preprocessing, execution and postprocessing.
    * Shared storage is accesible during the preprocessing and postprocessing steps but not during execusion.
* **Naming Convention**: Node class names should use **`PascalCase`** (e.g., `DataLoaderNode`, `TextProcessingNode`).

### 2. Flows
* **Definition**: A `Flow` is a declarative composition of `Nodes` that defines the sequence and logic of a workflow. It orchestrates how data moves between Nodes.
* **Purpose**: Flows represent the overall application logic, connecting individual computational steps into a cohesive pipeline.
* **Structure**:
    * Preferably, flows should be defined as factory functions with the following naming convention: `create_<name of the flow>_flow`.
    * The workflow logic is primarily defined using PocketFlow's declarative syntax (e.g., `node1 >> node2` for sequential execution, `[nodeA, nodeB]` for parallel).
* **Nesting**: Flows can be **nested** within other Flows or Nodes, allowing for complex, hierarchical workflow designs.
* **Naming Convention**:
    * Flow factory methods should follow the format `create_<name>_flow` (e.g., `create_hello_world_flow`).
    * Flow class names should use **`PascalCase`** (e.g., `MainProcessingFlow`, `RAGRetrievalFlow`).

### 3. Communication
* **Concept**: PocketFlow facilitates clear communication patterns between Nodes and Flows, often through explicit inputs and outputs, ensuring data integrity and traceability.

### 4. Advanced Concepts (Consider as needed)
* **Batch**: For processing data in batches efficiently.
* **Async**: For handling asynchronous operations within workflows.
* **Parallel**: For executing multiple Nodes or sub-Flows concurrently.

---

## General Python & PocketFlow Coding Standards ✒️

* **PEP 8 Compliance**: All generated Python code should strictly adhere to **PEP 8** style guidelines (e.g., indentation, line length, naming conventions for variables and functions).
* **Type Hinting**: Use **type hints** for all function arguments and return values to improve code readability and maintainability.
* **Docstrings**: All public Node, Flow, and significant method definitions should include **clear and concise docstrings** explaining their purpose, arguments, and return values.
* **Modularity**: Strive to keep Nodes and Flows focused on single responsibilities. Avoid creating monolithic components.
* **Imports**: Organize imports logically, typically using absolute imports for project modules and relative imports for sub-packages.
* **Error Handling**: Implement robust error handling within Nodes and Flows, catching expected exceptions and providing informative messages or logging.
* **Configuration**: Prefer external configuration (e.g., environment variables, config files) over hardcoding values within Nodes or Flows.

---

## Guiding Principles for Gemini CLI 🧭

When generating or modifying code for this project:

1.  **Prioritize PocketFlow Abstractions**: Always think in terms of Nodes and Flows for any computational or workflow task.
2.  **Adhere to Naming Conventions**: Ensure `PascalCase` for classes and `snake_case` for functions/methods and variables.
3.  **Favor Declarative Style**: When defining Flows, use PocketFlow's declarative chaining and composition mechanisms.
4.  **Provide Explanatory Comments/Docstrings**: Add comments for complex logic and thorough docstrings for all PocketFlow components.
5.  **Maintain Modularity**: Break down complex problems into smaller, manageable Nodes and Flows.

By following these guidelines, the Gemini CLI will produce Python code that is consistent with the PocketFlow framework and the project's coding standards.
