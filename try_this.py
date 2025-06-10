from dotenv import load_dotenv
import weaviate
import os
import sys

weaviate_url_envvar = "WEAVIATE_URL"
weaviate_api_key_envvar = "WEAVIATE_API_KEY"

try:
    load_dotenv()

    weaviate_url = os.getenv(weaviate_url_envvar)
    weaviate_api_key = os.getenv(weaviate_api_key_envvar)

    # Check if environment variables are set
    if not weaviate_url:
        print(f"Error: {weaviate_url_envvar} environment variable is not set.")
        sys.exit(1)
    if not weaviate_api_key:
        print(f"Error: {weaviate_api_key_envvar} environment variable is not set.")
        sys.exit(1)

    print(f"Attempting to connect to Weaviate at {weaviate_url}...")

    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=weaviate_url,
        auth_credentials=weaviate_api_key,
    )
    assert client.is_ready()
    weaviate_version = client.get_meta()["version"]
    print(f"Great! You are connected to Weaviate Cloud running version: {weaviate_version}, and all set up for the workshop.")
except Exception as e:
    print(f"Error connecting to Weaviate: {str(e)}")
    print(
        "Please check your environment variables, Weaviate cluster details, and internet connection."
    )
finally:
    try:
        client.close()
    except:
        # Handle the case where client wasn't initialized
        pass
