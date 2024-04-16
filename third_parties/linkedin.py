import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False, proxy_curl_api_key: str = None):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""

    # Get the profile from GitHub Gist (during development) to avoid sending too many get requests to the ProxyCurl API.
    # Parce que ça coute cher et malheureusement je ne suis pas riche!!
    LINKEDIN_URL = 'https://gist.githubusercontent.com/oozdal/15a23c0428f361beff94f02775492592/raw/7f880c0a51feb4c32ed1057d557e7bb1ba8382f3/ozer-ozdal.json'
    
    if mock:
        linkedin_profile_url = LINKEDIN_URL #os.environ.get("LINKEDIN_URL")
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        )
    else:
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        # header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
        header_dic = {"Authorization": f'Bearer {proxy_curl_api_key}'}
        response = requests.get(
            api_endpoint,
            params={"url": linkedin_profile_url},
            headers=header_dic,
            timeout=10,
        )

    data = response.json()

    # Unnecessary data cleaning
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data


if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/ozerozdal/",
            mock=True
        )
    )

