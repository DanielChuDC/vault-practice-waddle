from secrets import read_secret, write_secret

def main():
    # Example path and data for secret
    secret_path = 'secret/myapp/config'
    secret_data = {
        'database_url': 'mysql://user:password@hostname:port/database'
    }
    
    # Write secret to Vault
    write_secret(secret_path, secret_data)
    print("Secret written to Vault.")
    
    # Read secret from Vault
    retrieved_secret = read_secret(secret_path)
    print("Retrieved secret from Vault:")
    print(retrieved_secret)

if __name__ == "__main__":
    main()
