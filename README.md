# Interactive Workshop - Weaviate Agents

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
