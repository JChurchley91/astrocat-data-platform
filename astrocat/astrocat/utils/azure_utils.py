import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential


def get_key_vault_secret(secret_name: str, credential: DefaultAzureCredential) -> str:
    """
    Retrieve the key vault URL from config file and then retrieve a secret.
    Accepts a given secret name.
    Returns the secret value.
    """
    key_vault_url = os.getenv("KEY_VAULT_URL")
    # noinspection PyTypeChecker
    secret_client = SecretClient(vault_url=key_vault_url, credential=credential)
    secret = secret_client.get_secret(secret_name)
    return secret.value
