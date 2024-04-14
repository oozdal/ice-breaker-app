## Icebreaker

Icebreaker app finds the person on LinkedIn and provides a short and fun summary about that person. 
The purpose of this repo is nothing but to improve my Langchain skills with the help of an online course on Udemy taught by Eden Marco.

## Usage

1. **Provide API Keys**: Create a `.env` file in the root directory of the project and include the following API keys:

    ```python
    OPENAI_API_KEY="PUT_YOUR_OPENAI_API_KEY"
    PROXYCURL_API_KEY="PUT_YOUR_PROXYCURL_API_KEY"
    SERPAPI_API_KEY="PUT_YOUR_SERPAPI_API_KEY"
    ```

2. **Specify Person**: In the `ice_breaker.py` file, replace `"Ozer Ozdal"` with the name of the person you would like to search for on LinkedIn, and
provide a short description of that person to facilitate the search and summary generation process.

3. **Set Mock Flag**: Change the `mock` flag to `True` in the `ice_breaker.py` file. This will send a GET request using the PROXYCURL API.

4. **View Results**: After running `ice_breaker.py`, you can find the results in the `results/summary.json` file. The output will resemble the following:

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




