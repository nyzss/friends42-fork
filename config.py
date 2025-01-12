import os

# Secrets
update_key = os.environ.get("UPDATE_KEY")
secret = os.environ.get("SECRET_KEY")
key = os.environ.get("UID_KEY")
bocal_token = os.environ.get("UPDATE_KEY")
telegram_token = ''
sentry = ''

# Configuration
redirect_url = os.environ.get("REDIRECT_URL") + "/auth" if os.environ.get("REDIRECT_URL") else "http://localhost:8080/auth"
auth_link = f"https://api.intra.42.fr/oauth/authorize?client_id={key}&redirect_uri={redirect_url}&response_type=code&scope=public"
redis_host = os.environ.get("REDIS_HOST")
redis_port = os.environ.get("REDIS_PORT")
redis_password = os.environ.get("REDIS_PASSWORD")
campuses_to_update = [1]
sentry_traces_sample_rate = 0.4
sentry_profiles_sample_rate = 0.4
