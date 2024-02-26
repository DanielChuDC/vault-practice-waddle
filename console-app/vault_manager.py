import hvac

def get_vault_client():
    # Connect to the Vault server
    client = hvac.Client(url='http://localhost:8200')
    
    # Check if authentication method is required (e.g., token authentication)
    if not client.is_authenticated():
        # Authenticate with your Vault server 
        client.token = 'hvs.p1eQEJJN6AVeN0ZUnogy5h15'
        if not client.is_authenticated():
            raise Exception("Failed to authenticate with Vault")
    
    return client
