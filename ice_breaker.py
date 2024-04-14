from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile
import os, json


if __name__ == "__main__":
    load_dotenv()

    print("Hello LangChain!")
    
    information = """
    Ozer Ozdal is an ML Engineer with many years of expertise in designing 
    and implementing machine learning solutions,
    predictive analytics, and data science applications. 
    Demonstrated proficiency in model explainability, including LLM models, 
    and a robust comprehension of machine learning algorithms for classification, regression, 
    and clustering, driving toward strategic business objectives. 
    Skilled in leveraging AWS cloud architectures. 
    Proficient in employing data-centric methodologies to extract insights and drive decision-making.
    """

    linkedin_profile_url = linkedin_lookup_agent(name="Ozer Ozdal")

    summary_template = """
    given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    # temperature will decide how creative the language model will be.
    # 0 means it won't be creative
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url=linkedin_profile_url, 
        mock=True)

    summary = chain.invoke(input={"information": linkedin_data})

    #print(summary['information'])
    print(summary['text'])

    # Save the summary
    with open("results/summary.json", "w") as outfile:
        json.dump(summary, outfile)
