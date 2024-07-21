import boto3
import requests
from jose import JWTError, jwt, jwk
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

cognito_region = "ap-northeast-1"
cognito_user_pool_id = "ap-northeast-1_ceN7jDgk2"
cognito_client_id = "6jhdrjmqpuplq33ravcvbgaavh"

def get_cognito_client():
    return boto3.client("cognito-idp", region_name=cognito_region)


def get_jwks():
    url = f"https://cognito-idp.{cognito_region}.amazonaws.com/{cognito_user_pool_id}/.well-known/jwks.json"
    response = requests.get(url)
    return response.json()

def get_public_key(jwks, kid):
    for key in jwks['keys']:
        if key['kid'] == kid:
            return jwk.construct(key)
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Public key not found"
    )

def get_user_info_from_id_token(id_token: str):
    try:
        jwks = get_jwks()
        unverified_header = jwt.get_unverified_header(id_token)
        rsa_public_key = get_public_key(jwks, unverified_header['kid'])
        payload = jwt.decode(id_token, rsa_public_key, algorithms=['RS256'], audience=cognito_client_id)
        user_info = {
            "cognito_id": payload["sub"],
            "email": payload["email"]
        }
        return user_info
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

async def get_current_user(token: str = Depends(oauth2_scheme)):
    return get_user_info_from_id_token(token)