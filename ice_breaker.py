from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile
import streamlit as st
import json


if __name__ == "__main__":
    load_dotenv()

    # Streamlit app
    st.subheader("Get a summary of the person you'd to break the ice with")
                
    print("Hello LangChain!")

    default_name = "Ozer Ozdal"  # Default value for the Name input

    name = st.text_input("Name", default_name)
    
    default_info = """Ozer Ozdal is an ML Engineer with many years of expertise in designing and implementing machine learning solutions, predictive analytics, and data science applications.
    Demonstrated proficiency in model explainability, including LLM models, and a robust comprehension of machine learning algorithms for classification, regression, and clustering, driving toward strategic business objectives. Skilled in leveraging AWS cloud architectures. 
    Proficient in employing data-centric methodologies to extract insights and drive decision-making."""

    information = st.text_area("Provide some information about the person you would like to search", default_info)

    if st.button("Submit"):
        try:

            if name == default_name:
                # If the user searches "Ozer Ozdal", do not send API requests.
                # Fetch the information from the results/summary.json file as a cost-conscious application
                with open("results/summary.json") as f:
                    summary = json.load(f)
                    st.success(summary['text'])

            else:
                linkedin_profile_url = linkedin_lookup_agent(name=name)

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

                # Return the short summary and two interesting facts about the person
                st.success(summary['text'])

        except Exception as e:
            st.error(f"An error occurred: {e}")
            
