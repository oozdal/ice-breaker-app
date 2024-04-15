## Icebreaker Streamlit Application

Icebreaker app finds the person on LinkedIn and provides a short and fun summary about that person. 
The purpose of this repo is nothing but to improve my Langchain skills with the help of an online course on Udemy taught by Eden Marco.

## Usage & Streamlit User Interface

1. **Provide API Keys**: Create a `.env` file in the root directory of the project and include the following API keys:

    ```python
    OPENAI_API_KEY="PUT_YOUR_OPENAI_API_KEY"
    PROXYCURL_API_KEY="PUT_YOUR_PROXYCURL_API_KEY"
    SERPAPI_API_KEY="PUT_YOUR_SERPAPI_API_KEY"
    ```

2. **Run the App and Specify Person**:

```python
streamlit run ice_breaker.py
```

- Replace `"Ozer Ozdal"` with the name of the person you would like to search for on LinkedIn.
- Additionally, please provide a brief description of the person to help the search and summary creation process. 
- Once done, click the submit button as shown in the example below. Enjoy!

![Screenshot 2024-04-15 at 2 56 22 PM](https://github.com/oozdal/ice-breaker-app/assets/34719109/261f74b5-b9be-424e-986e-7997debe4829)

## A Cost-Conscious Approach

**Set Mock Flag**: To search for someone other than Ozer Ozdal, simply update the `mock` flag to False in the `ice_breaker.py` file. This action will trigger a GET request to the PROXYCURL API. 
- Extra Info: I enable the `mock` flag and set it to `True` to send a GET request to GitHub Gist, fetching a saved JSON version of my LinkedIn page, as a cost-conscious measure.
- This approach helps me minimize the number of API requests sent to the PROXYCURL API during the development phase and save money.

## Some Screenshots From the Development Phase

```console
Hello LangChain!

> Entering new AgentExecutor chain...
I should use the tool to search for the LinkedIn profile page of Ozer Ozdal.
Action: Crawl Google for LinkedIn profile page
Action Input: Ozer Ozdal LinkedIn profile https://ca.linkedin.com/in/ozerozdal
I have found the LinkedIn profile page for Ozer Ozdal.
Final Answer: https://ca.linkedin.com/in/ozerozdal

> Finished chain.

1. **Summary:**
   - **Name:** Özer Özdal, Ph.D
   - **Occupation:** Data Scientist at GoldSpot Discoveries Corp.
   - **Location:** Montreal, Quebec, Canada
   - **Education:** Ph.D in Physics from Concordia University
   - **Languages:** English, Turkish, French
   - **Experience:** Worked as a Data Scientist at GoldSpot Discoveries Corp. and Breathe BioMedical, and as a Postdoctoral Researcher at Concordia University
   - **Accomplishments:** Published several scientific papers related to new physics beyond the Standard Model and received awards like the Mitacs Globalink Research Award Abroad

2. **Interesting Facts:**
   - Özer Özdal has collaborated with Benjamin Fuks on several phenomenological studies.
   - Özer Özdal has received the Mitacs Globalink Research Award Abroad to support research-related costs and intern travel costs.
```

## Technologies Used

- **Langchain**: Integrated for processing language and generating concise summaries.
- **OpenAI API**: Utilized for generating summaries about individuals.
- **ProxyCurl API**: Used for making requests to LinkedIn.
- **SerpAPI**: Employed for scraping search engine results.

## Deployment

- Icebreaker is an ongoing project. I will deploy the app on Render soon. Stay tuned!

