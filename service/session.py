import pickle
import os


def create_user(name, email, password):
    try:
        user = firebase_auth.create_user(
            email=email, password=password, display_name=name
        )
        return user.uid
    except:
        return None


def login_user(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return user["idToken"]
    except:
        return None


def store_session(token):
    if os.path.exists("token.pickle"):
        os.remove("token.pickle")
    with open("token.pickle", "wb") as f:
        pickle.dump(token, f)


def load_token():
    try:
        with open("token.pickle", "rb") as f:
            token = pickle.load(f)
        return token
    except:
        return None


def authenticate_token(token):
    try:
        result = firebase_auth.verify_id_token(token)

        return result["user_id"]
    except:
        return None


def get_name(token):
    try:
        result = firebase_auth.verify_id_token(token)

        return result["name"]
    except:
        return None


def revoke_token(token):
    result = firebase_auth.revoke_refresh_tokens(authenticate_token(token))
    if os.path.exists("token.pickle"):
        os.remove("token.pickle")
