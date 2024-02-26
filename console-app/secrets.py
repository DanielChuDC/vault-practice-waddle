from vault_manager import get_vault_client

def read_secret(path):
    # Initialize Vault client
    client = get_vault_client()
    
    # Read secret from Vault
    secret = client.secrets.kv.read_secret_version(path=path)
    
    # Extract and return secret data
    if secret:
        return secret['data']['data']
    else:
        return None

def write_secret(path, data):
    # Initialize Vault client
    client = get_vault_client()
    
    # Write secret to Vault
    client.secrets.kv.v2.create_or_update_secret(path=path, secret=data)
