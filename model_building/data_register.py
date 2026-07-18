from huggingface_hub.utils import RepositoryNotFoundError, HfHubHTTPError
from huggingface_hub import HfApi, create_repo, upload_folder
import os

# HF repo details , repo_id is the repo space created in Hugging Face
repo_id = "SubashChandraNaik/Tourism-Project-v1"
repo_type = "dataset"

hf_token = os.getenv('HF_TOKEN', '').strip()
if not hf_token:
    raise ValueError("HF_TOKEN is not set or is empty")
# Initialize API client( this is the token generated in HF is stort as HF_TOKEN in google colab)
api = HfApi(token=hf_token)

# Step 1: Check if the space exists
try:
    api.repo_info(repo_id=repo_id, repo_type=repo_type)
    print(f"Space '{repo_id}' already exists. Using it.")
except RepositoryNotFoundError:
    print(f"Space '{repo_id}' not found. Creating new space...")
    create_repo(repo_id=repo_id, repo_type=repo_type, private=False)
    print(f"Space '{repo_id}' created.")

# Validate directory exists
if not os.path.isdir(data_path):
    raise FileNotFoundError(f"Data directory not found: {data_path}")
    
api.upload_folder(
    folder_path="Tourism-Project/data",
    repo_id=repo_id,
    repo_type=repo_type
)
