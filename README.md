# Interactive Workshop - Weaviate Agents

## Introduction

### What are Agents?

An **agent** can perform tasks with some degree of autonomy - i.e. it can make some decisions itself, rather than being driven by a set of rules.

This makes agents powerful tools as a part of a system, especially for tasks that cannot be easily expressed as a set of rules.

### What are Weaviate Agents?

Weaviate Agents are a set of specialized, pre-built agentic services designed for specific tasks. They are designed to work with Weaviate, an AI-native database, to simplify data engineering and AI development workflows.

#### Query Agent

The Weaviate Query Agent is a pre-built agentic service designed to answer natural language queries based on the data stored in Weaviate Cloud.

The user simply provides a prompt/question in natural language, and the Query Agent takes care of all intervening steps to provide an answer.

<center><img src="img/query_agent_architecture_light.png" width="90%"></center>

#### Transformation Agent

The Weaviate Transformation Agent is an agentic service designed to augment and transform data using generative models. Use the Transformation Agent to append new properties and/or update existing properties of data on existing objects in Weaviate.

<center><img src="img/transformation_agent_overview_light.png" width="90%"></center>

#### Personalization Agent

The Weaviate Personalization Agent is an agentic service designed to return personalized recommendations tailored to each user. The Personalization Agent uses data from the associated Weaviate Cloud instance to provide these recommendations.

<center><img src="img/personalization_agent_overview_light.png" width="90%"></center>

### Notes and limitations

All Weaviate Agents are in technical preview (do **not** use them in production)

<center><img src="img/agents_tech_preview.png" width="60%"></center>

> ⚠️ The Weaviate Transformation Agent modifies data objects in Weaviate. **Be extremely careful in using it.**
>
> The Agent may not work as expected, and the data in your Weaviate instance may be affected in unexpected ways.

## Student steps

### Create a Weaviate Cloud cluster

Go to [Weaviate Cloud](https://console.weaviate.cloud/) and create a Sandbox cluster (free for 14 days). If you don't have an account, you can sign up for free.

- Any region with default settings is fine.
    - Note: As of Weaviate 1.31, RBAC is enabled by default.
- Take note of the cluster URL
- Wait for the cluster to be ready (it may take a minute or two).
- Create an API key for the cluster:
    - Scroll down to "API Keys" under "Cluster details" and click "Create API Key".
    - Provide a name (e.g. "admin-key") and select "admin" as the role.
    - Click "Create"
    - IMPORTANT: Copy the API key and save it somewhere safe. You can also download it locally. You won't be able to see it again.
- Set up the `.env` file
    - Copy `.env.example` to `.env`
    - Fill in the `WEAVIATE_URL` with your cluster URL.
    - Add the API key to the `.env` file as `WEAVIATE_API_KEY`.
- You are now ready to run the code (`wv-*.ipynb`) for the tutorial!

### Set up your Python environment

- Set up your preferred Python environment
    - e.g. Set up a virtual environment (optional but recommended):
    ```bash
    python -m venv .venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```
    - Or use `uv`, `conda`, or any other environment manager you prefer.
- Create a Weaviate Cloud cluster as described above.
- Set up the `.env` file as described above

### Test your setup

Run `try_this.py` to test your setup.

```bash
python try_this.py
```

If everything is set up correctly, you should see a message like this, indicating that the connection to Weaviate was successful.

```plaintext
Attempting to connect to Weaviate at 3kxk7cmssrkyhjdbuijvg.c0.europe-west3.gcp.weaviate.cloud...
Great! You are connected to Weaviate Cloud running version: 1.31.0, and all set up for the workshop.
```
