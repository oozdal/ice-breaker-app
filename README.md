## Icebreaker Streamlit Application

Icebreaker app finds the person on LinkedIn, scraps the person's LinkedIn page and then provides a short summary and two interesting facts about that person. 
The purpose of this repo is nothing but to improve my Langchain skills with the help of an online course on Udemy taught by Eden Marco.

## Usage, Deployment & Streamlit User Interface

The application is deployed and accessible at: [Ice Breaker App](https://ice-breaker-app.onrender.com/)

Warning: Free Instance Spin-Down Delay

Please note that the free instance provided by Render may experience spin-down due to inactivity. This could result in delays of 50 seconds or more when processing requests. Please be patient while your web browser tries to load the page.

**Provide the following API Keys and Specify Person**:

- Provide your API Keys on the left side of the User Interface.
- Replace `"Ozer Ozdal"` with the name of the person you would like to search for on LinkedIn.
- Additionally, please provide a brief description of the person to help the search and summary creation process. 
- Once done, click the submit button as shown in the example below. Enjoy!

![Screenshot 2024-04-15 at 2 56 22 PM](https://github.com/oozdal/ice-breaker-app/assets/34719109/261f74b5-b9be-424e-986e-7997debe4829)

- If you try to search someone without providing your API Keys, you will receive an error similar to the following.

![Screenshot 2024-04-16 at 12 27 49 AM](https://github.com/oozdal/ice-breaker-app/assets/34719109/1c1ae22a-7ffe-4722-8895-8f427905e31b)


## A Cost-Conscious Approach

**Set Mock Flag**: To search for someone other than Ozer Ozdal, simply update the `mock` flag to False in the `ice_breaker.py` file. This action will trigger a GET request to the PROXYCURL API. 
- Extra Info: I enable the `mock` flag and set it to `True` to send a GET request to ![GitHub Gist](https://gist.githubusercontent.com/oozdal/15a23c0428f361beff94f02775492592/raw/7f880c0a51feb4c32ed1057d557e7bb1ba8382f3/ozer-ozdal.json), 
fetching a saved JSON version of my LinkedIn page, as a cost-conscious measure.
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

