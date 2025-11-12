import os

# Load all secrets from GitHub Actions environment variables
NAUKRI_USERNAME = os.getenv("NAUKRI_USERNAME")
NAUKRI_PASSWORD = os.getenv("NAUKRI_PASSWORD")
NAUKRI_MOBILE = os.getenv("NAUKRI_MOBILE")

# Paths for resume files (safe defaults if not provided)
NAUKRI_ORIGINAL_RESUME_PATH = os.getenv("NAUKRI_ORIGINAL_RESUME_PATH", "./resume.pdf")
NAUKRI_MODIFIED_RESUME_PATH = os.getenv("NAUKRI_MODIFIED_RESUME_PATH", "./resume_mod.pdf")

# URLs
NAUKRI_LOGIN_URL = "https://www.naukri.com/nlogin/login"
NAUKRI_PROFILE_URL = "https://www.naukri.com/mnjuser/profile"

# Selenium headless mode
HEADLESS = True
