import streamlit as st
from PIL import Image

favicon = Image.open("images/robot-icon2.png")
st.set_page_config(page_title="Concept and Architecture", page_icon=favicon,layout="wide", initial_sidebar_state="expanded")

# Read the contents from the CSS file
with open("css/styles.css", "r") as f:
    css = f.read()

# Include the CSS in the Streamlit app
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


# Sidebar content providing brief overviews of each page
# Augmenting Skills (Page 6)
st.sidebar.header("Augmenting Skills")
st.sidebar.write("""
Learn how Generative AI can augment your skills across various professional roles, 
from software engineering to human resources.
""")

# Single-User APP (Page 3)
st.sidebar.header("Single-User APP")
st.sidebar.write("""
Explore the architecture and mechanics of a single-user AI orchestrator application,
tailored for individual users.
""")

# This Application (Page 1)
st.sidebar.header("This Application")
st.sidebar.write("""
Understand the components and design of this application, which mimics some 
features of a multi-tenant generative AI orchestrator.
""")

# Prompt Design (Page 4)
st.sidebar.header("Prompt Design")
st.sidebar.write("""
Dive into the art of crafting effective prompts for generative AI and learn what to avoid
in the design of a Generative AI APP.
""")

# Architecture (Page 2)
st.sidebar.header("Architecture")
st.sidebar.write("""
Get insights into the architecture design of a multi-tenant orchestrator for Generative Pre-trained Transformers (GPT).
""")

# Architecture (Page 6)
st.sidebar.header("Chain Of Thought")
st.sidebar.write("""
Guide the model towards specific types of responses or extract particular kinds of knowledge.
""")

st.sidebar.success("""
To switch page, select a tab on the right.
""")

# st.title("Concept and Architecture")

# Function for Page 1
def page_5():
    st.markdown("""
                # Augmenting Skills
## The Journey to Augmenting Skills Using Generative AI in Various Roles
In today's fast-paced technological landscape, simply being an expert in your domain is not enough. Whether you are a software engineer, HR professional, scientist, salesperson, or a finance expert, the key to staying competitive lies in your ability to harness tools that can augment your skills. One such tool is Generative AI, like GPT-4, which can assist you across a multitude of tasks, from writing code to crafting persuasive sales pitches. But the power of AI doesn't just lie in its computational abilities—it's in how well you can communicate with it.
## Benefits by Role
### Software Engineer
- **Code Reviews**: Use AI to automatically flag potential issues or inefficiencies in your code.
- **Debugging**: Generate potential solutions or workarounds for identified bugs.
### Human Resources
- **Resume Screening**: Automate the initial steps of screening resumes and shortlisting candidates.
- **Employee Onboarding**: Generate customized onboarding documents tailored to the new hire's role.
### Finance
- **Risk Assessment**: Generate comprehensive risk reports based on various financial indicators.
- **Quarterly Reports**: Automate the preparation of quarterly financial statements and reports.
### Sales
- **Client Pitches**: Prepare highly customized sales pitches for different client profiles.
- **Email Campaigns**: Generate persuasive and effective email content tailored to different audience segments.
### Scientist
- **Data Analysis**: Automate the initial steps of data preprocessing and analysis.
- **Research Summaries**: Generate concise summaries of academic papers or internal research documents.
## Starting Small: You Don’t Have to Be a "Prompt Engineer"
You don't need to start big. Begin by integrating AI into your daily routine through a handful of tasks. Here are some ways to start small:

- **Automated Responses**: Draft a few prompt templates for automated email responses for common queries.
- **Data Summaries**: Use prompt templates to generate quick summaries of large datasets or complex financial statements.
- **Meeting Notes**: Use AI to transcribe and summarize key points from meetings.

You don't need to be an expert in crafting prompts. There are numerous templates and examples available that you can tweak according to your needs.
## Where Most People Are Today and Where They Could Be
### Current State
Most professionals today are experts in their respective domains but are yet to fully leverage the power of AI to augment their skills. They are generally bogged down by repetitive tasks, time-consuming data analysis, and the constant need to stay updated.
### Future State
By incorporating AI, not only can they automate mundane tasks, but they can also bring a level of sophistication and customization to their work that was previously unimaginable. Mastering the art of effective prompting allows for a symbiotic relationship with AI, transforming not just productivity but also the quality of work.
### The Balanced Approach: Benefits and Risks
While the benefits of augmenting your skills with AI are substantial, it's equally important to be mindful of the risks such as data privacy and ethical considerations. Utilize AI responsibly to not just protect yourself and your organization but also contribute to a more equitable technological future.

So, if you're looking to supercharge your career, start thinking of Generative AI not just as a tool but as a collaborative partner that speaks your language. Master the art of effective prompting and you'll unlock capabilities you never knew you had.

                """)

# Function for Page 2
def page_3():
    st.markdown("""
# This Single-User APP
I wrote about [*Unleashing the Power of Generative AI in Your Career: It's Not Just About Knowledge, It's About Language*](https://datatunnel.io/2023/08/27/unleashing-the-power-of-generative-ai-in-your-career/), initially published on August 27, 2023, at datatunnel.io. I delve into the transformative potential of generative AI in augmenting human skills across various professional domains—from software engineering and human resources to finance and sales. 

However, the article argues that the real power of these AI models is not merely their extensive knowledge base, but in the user's ability to effectively communicate with them. In AI parlance, knowing how to craft the perfect "prompts" can unlock highly tailored and context-specific solutions, supercharging productivity. While highlighting the golden use cases where generative AI excels, the article also emphasizes the importance of understanding the associated risks and ethical considerations. __The key takeaway is that using generative AI responsibly and to your maximum benefit is not just about what the AI knows; it's about knowing how to ask questions.__

## Unveiling the Single User AI Orchestrator Application

As you continue reading, we'll take a deep dive into the mechanics of the *Single User AI Orchestrator Application*—a simplified yet potent platform that mimics some of the core functionalities of a multi-tenant generative AI orchestrator. Tailored for individual users, this application serves as a bridge between you and an array of advanced AI models, making your interactions more personalized, efficient, and context-aware.

You'll get insights into the key components that make up this orchestrator, including the User Interface for seamless interaction, the Orchestrator that serves as the nerve center for AI-user engagement, and the API Models that power the generative responses. We'll also touch upon the Elasticsearch Database, a robust storage and search mechanism that keeps track of your historical interactions for more meaningful future engagements.

You'll learn how Python and Streamlit UI come together to create an interactive web application that not only makes it easy for you to engage with AI but also enriches the quality of those engagements.

In essence, the Single User AI Orchestrator Application is engineered to offer you a personalized and efficient experience with AI systems. By utilizing pre-trained language models and state-of-the-art search functionalities, the application aims to furnish you with accurate and contextually relevant responses, all within a user-friendly interface.

So, prepare to explore how this application can become your personalized AI assistant, amplifying your productivity and decision-making in an intuitive environment.

## An Invitation to the Opensource Community

As we stand on the cusp of a new era in human-AI collaboration, the Single User AI Orchestrator Application offers a glimpse into the future of personalized and efficient interactions with generative AI systems. However, the vision is far grander—a robust, scalable, and secure multi-tenant orchestrator capable of serving diverse user needs across various domains. Achieving this vision is not a solitary endeavor but a collaborative one.

We extend a warm invitation to the open-source community to join us in this exciting journey. Your expertise in design, architecture, and software development can immensely contribute to building a software stack that is not only more robust but also capable of supporting a multi-tenant orchestrator. Together, we can push the boundaries of what is possible in the realm of generative AI, building tools that are not only powerful but also ethical, responsible, and inclusive.

By pooling our collective skills and knowledge, we can accelerate the development of a system that could revolutionize the way we interact with AI, setting new industry standards for performance, security, and usability. Let's come together to create a future where generative AI serves as an extension of human capability, making our lives not just easier, but also profoundly enriched.

Thank you for your interest, and we look forward to your valuable contributions to this groundbreaking project.

             """)

# Function for Page 3
def page_1():
    # Display a Data retention notice as of OpenAI's policy change on 1 March 2023
    st.markdown("""
    ### Privacy and Data Retention ###
    OpenAI is trained up till January 2022. The application was tested using OpenAI model releases of 13 June 2023. As of March 1, 2023, data sent to the OpenAI API will not be used to train or improve OpenAI models (unless you explicitly [opt in](https://docs.google.com/forms/d/e/1FAIpQLSevgtKyiSWIOj6CV6XWBHl1daPZSOcIWzcUYUXQ1xttjBgDpA/viewform)).
    Please review [OpenAI API Policies](https://openai.com/policies) for more information.
    """, unsafe_allow_html=True)

    st.markdown("""
# This Application
Our application is a typical thin-layer application for a single user which demonstrates some components of a multi-tenant generative AI orchestrator, including a user search memory, allowing to revisit previous iterations with a particular AI model.

A single user orchestrator is a software component that manages the interaction between a user and an AI system. It is designed to handle requests from a single user and provide personalized responses based on the user's prompt context and history. The implementation of a single user orchestrator typically involves several components, including: 

1. **User Interface**: This component provides the user with a way to interact with the system, such as a web or mobile application. 
1. **Orchestrator**: This component manages the interaction between the user and the AI system. It receives requests from the user, selects the appropriate API model to use, and generates a response based on the user's context and history.
1. **API Models**: These are pre-trained language models that are used to generate responses to user requests. In this example, the OpenAI API is used to provide access to several API models, including gpt-3.5-turbo, gpt-3.5-turbo-16k, gpt-4, and gpt-4-32k.
1. **Elasticsearch Database**: This component is used to store and retrieve data related to the user's context and history. It provides fast and efficient search capabilities and can be used to store a wide range of data types, including text, numerical data, and geospatial data.
1. **Python**: This is a programming language that is commonly used for AI development. It is used to write the code that implements the various components of the single user orchestrator. 
1. **Streamlit UI**: This is a Python library that is used to create interactive web applications. It provides a simple and intuitive way to create user interfaces for AI systems.

The main components of the single user orchestrator include the user interface, orchestrator, API models, and Elasticsearch database. The user interface provides the user with a way to interact with the system, while the orchestrator manages the interaction between the user and the AI system. The API models are used to generate responses to user requests, and the Elasticsearch database is used to store and retrieve data related to the user's context and history. 

Overall, the single user orchestrator is designed to provide a personalized and efficient way for users to interact with AI systems. By leveraging pre-trained language models and advanced search capabilities, it can generate accurate and relevant responses to user requests, while also providing a seamless and intuitive user experience.
## Application Architecture
![Single-User-Orchestrator Image](https://datatunnel.io/wp-content/uploads/2023/08/single-user-ai-augments.png)             """)

# Function for Page 4
def page_4():
    st.markdown("""
# Prompt Design
## Generative AI Models – what can they do?
LLM (Large Language Model) models are pre-trained language models that can be fine-tuned for specific tasks. These models are designed to understand natural language and generate human-like responses to user requests. Some of the common LLM models and tasks include: 

1. **Question-Answering**: This involves answering questions posed by users, such as "What is the capital of France?" or "Who won the Nobel Prize in Physics in 2020?".
1. **Text Summarization**: This involves generating a summary of a longer text, such as an article or a book.
1. **Translation**: This involves translating text from one language to another, such as from English to Spanish or from Chinese to French.
1. **Sentiment Analysis**: This involves analyzing the sentiment of a piece of text, such as whether it is positive, negative, or neutral.
1. **Named Entity Recognition**: This involves identifying and extracting named entities from a piece of text, such as people, places, and organizations.
1. **Chatbot Functionality**: This involves creating a chatbot that can interact with users in a natural and human-like way.
1. **Content Creation**: This involves generating creative content, such as articles, essays, or stories.
1. **Education**: This involves providing educational content and tutoring in various subjects.
1. **Programming**: This involves writing, debugging, or explaining code, and performing code-related tasks or calculations.
1. **Research Assistance**: This involves summarizing research papers or articles, providing insights or explanations on specific topics, and assisting with research tasks.

LLM models can be fine-tuned for specific tasks by providing them with training data that is relevant to the task. For example, to fine-tune an LLM model for question-answering, the model can be trained on a dataset of questions and answers. Similarly, to fine-tune an LLM model for sentiment analysis, the model can be trained on a dataset of text with labeled sentiment. By fine-tuning LLM models for specific tasks, they can be used to generate more accurate and relevant responses to user requests.

## What shall be avoided when designing a Generative AI APP?
When designing a Generative AI APPs, it is important to avoid potential risks and biases that may arise from the use of large language models. Some of the things that should be avoided include: 

- Allowing the model to generate inappropriate or harmful content
- Over-reliance on the model's output without human oversight
- Failure to consider the potential risks and biases associated with the model's training data
- Ignoring the ethical implications of using large language models
- Failing to implement AI safety principles in your APP, can lead to uncensored prompt responses.
- Failing to provide transparency and accountability in the model's decision-making process. 

These risks can be mitigated by implementing guardrails during training, such as data filtering and training objectives, and by using human editors to review and edit the model's output. Additionally, it is important to consider the legal and regulatory compliance requirements when developing generative apps.

## Approach to Controlled Prompt Design
A good approach to building a prompt involves several steps, including: 

1. **Identifying the primary focus of the prompt**: This involves determining the main topic or goal of the prompt, such as answering a specific question or providing information on a particular subject.
1. **Defining the context focus**: This involves specifying the context in which the prompt will be used, such as the user's location, preferences, or previous interactions with the system. 
1. **Creating the context information**: This involves providing the system with the necessary information to generate an accurate response, such as the user's name, age, or location. 
1. **Crafting the system message**: This involves creating a message that introduces the prompt and sets the tone for the interaction. 
1. **Writing the primary focus**: This involves providing the user with the information they need to achieve their goal, such as answering their question or providing them with relevant information. 
1. **Adding clarification prompts**: This involves anticipating potential misunderstandings or ambiguities in the user's request and providing additional prompts to clarify their intent.
1. **Handling invalid tasks**: This involves providing the user with an appropriate response if their request cannot be fulfilled, such as asking for more information or suggesting an alternative approach. 
1. **Validating responses**: This involves verifying that the user's response is accurate and appropriate, and taking appropriate action if it is not. The main parts of a prompt include the system message, primary focus, context focus, context information, and response validation. The sub-parts of each of these components will vary depending on the specific prompt and the context in which it is used. For example, the context information may include the user's name, age, and location, while the response validation may involve checking the user's response against a database of valid responses.

![Prompt Design Image](https://datatunnel.io/wp-content/uploads/2023/08/prompt-structure-ai-augments.png)

                """)

def page_2():
    st.markdown("""
# Architecture Design of a Multi-Tenant Orchestrator for Generative Pre-Trained Transformer (GPT)
Generative AI models have expanded beyond the realm of academic research to practical applications in various industries. Whether it's automating customer service, generating content, or assisting in data analytics, the versatility of these models is truly transformative. However, as organizations scale their AI deployments to serve a diverse user base, the complexity of managing these systems grows exponentially. This is where the concept of a multi-tenant orchestrator comes into play.

A multi-tenant orchestrator is an advanced system designed to manage the intricacies of deploying generative AI applications across multiple users or tenant groups. Its architecture is modular, with each component serving a specific function in the AI application workflow. [Simon Attard](https://www.linkedin.com/in/simonattard/) introduced these concepts on June 20, 2023 in his article about [Leveraging Large Language Models in your Software Applications](https://medium.com/@simon_attard/leveraging-large-language-models-in-your-software-applications-9ea520fb2f34). The main conceptual components include:
## Components
1. **Task Planner**: Acts as the control hub for task management. Its intakes user requests and maps out the appropriate actions to be executed by the system.
1. **Context Store**: Holds the contextual information of each user, including their past interactions, preferences, and behavioral history, to enable more personalized and relevant interactions.
1. **Memory Store**: Stores the prompt and response pairs generated during previous sessions, aiding in maintaining a consistent and coherent interaction over time.
1. **Prompt Manager**: Determines the most suitable prompt to present to the user, drawing from their context and the tasks identified by the Task Planner.
1. **Response Manager**: Validates and interprets the user's response and decides on the subsequent actions or responses to be generated.
1. **Evaluation**: Monitors and stores performance metrics and user feedback to continually refine the system's effectiveness and reliability.
1. **LLM Provider**: Functions as the gateway to the underlying Language Learning Models (LLMs), providing the computational power for generating human-like responses.
1. **User Interface**: Serves as the front-end through which users interact with the system, which could be a web application, a mobile app, or another interface.
## Responsibilities
The multi-tenant orchestrator's role is not just limited to managing these components. It also takes on the crucial tasks of:

- **User Segmentation**: It can serve multiple users or groups of users (tenants), each with their own customized experience, skills, language and AI use cases.
- **Personalization**: By drawing from components like Context Store and Memory Store, it ensures that each user's interaction is personalized and contextually relevant.
- **Privacy and Security**: The orchestrator ensures that user data, including memories and context, are securely stored and accessed only by authorized entities.
- **Performance Optimization**: Through its Evaluation component, the orchestrator focuses on continual improvement, ensuring that the system performs efficiently and meets user expectations.

![Architecture Image](https://datatunnel.io/wp-content/uploads/2023/08/multi-user-ai-augments.png)

:orange[The main difference between a single user orchestrator and a multi-tenant orchestrator is that the latter is designed to handle requests from multiple users as well as a user request can deal with a chain of subtasks.] This requires additional functionality to manage user context and history, as well as to ensure that each user's data is kept separate and secure. By leveraging pre-trained language models and advanced search capabilities, a multi-tenant orchestrator can generate accurate and relevant responses to user requests, while also providing a seamless and intuitive user experience for multiple users.

By efficiently chaining these components together, the multi-tenant AI orchestrator serves as the backbone of scalable and secure generative AI applications, ensuring that each user's interaction is not just responsive but also personalized and secure.

## Chain of Tasks
Use prompt collection templates as inputs to create a "Chain of Tasks" template in JSON that uses collection_id and usermessage_id as inputs. The "chain of tasks is another JSON schema stored in your database environment. For instance, a chain of tasks defines a logical execution and link a chain of prompt templates [collection_id, usermessages_id] in a specific execution order. A ChainOfTask schema may have TaskGroupID as unique identifier and SubTasks which link back to __Collection Record__ using collection_id and usermessage_id keys.

### Task Chain Schema

```
{
  "TaskChainID": 1,
  "TaskChainName": "Data Migration and Integrity Checks",
  "TaskChainDescription": "This task chain aims to integrate Salesforce and Workday data and check for integrity.",
  "SubTasks": [
    {
      "SubTaskID": 1,
      "CollectionID": "col-20230904220737",
      "UserMessageID": 1,
      "InputParameters": "[Account, Field1]"
    },
    {
      "SubTaskID": 2,
      "CollectionID": "col-20230904220737",
      "UserMessageID": 2,
      "InputParameters": "[Worker, Field2]"
    },
    {
      "SubTaskID": 3,
      "CollectionID": "another-collection-id",
      "UserMessageID": 5,
      "InputParameters": "[SomeOtherObject, SomeOtherField]"
    }
  ],
  "ExecutionOrder": [1, 2, 3],
  "CreatedAt": "2023-09-06T12:34:56Z",
  "CreatedBy": "username_here",
  "LastUpdated": "2023-09-06T13:00:00Z",
  "LastUpdatedBy": "another_username_here"
}
```

### Task Chain Execution Schema
TaskChain schemas collections are a set of LLM subtasks that complete a main task. When a user designs a TaskChain template (based on prompt collections Templates) then for the purpose of the TaskChain execution a new schema will be created that tracks execution of chained tasks. Each subtask stores transactional data. When a previous subtask has stored its results on the document database, it should track its unqiue DOC-ID. In addition, each subtask tracks temporal and status data such as start time, completion time and completion status (idle, running, completed, failed).

````
{
  "TaskChainID": 1,
  "TaskChainName": "Data Migration and Integrity Checks",
  "TaskChainDescription": "This task chain aims to migrate Salesforce and Workday data and check for integrity.",
  "SubTasks": [
    {
      "SubTaskID": 1,
      "CollectionID": "col-20230904220737",
      "UserMessageID": 1,
      "InputParameters": "[Account, Field1]",
      "ExecutionInfo": {
        "StartTime": "2023-09-06T14:34:56Z",
        "EndTime": "2023-09-06T14:35:30Z",
        "Status": "completed",
        "ElasticSearchDocID": "doc-12345"
      },
      "ContextInformation": {
        "PreviousContext": null,
        "CurrentContext": "Textual context data for current context taken from Context Store..."
      }
    },
    {
      "SubTaskID": 2,
      "CollectionID": "col-20230904220737",
      "UserMessageID": 2,
      "InputParameters": "[Worker, Field2]",
      "ExecutionInfo": {
        "StartTime": "2023-09-06T14:36:00Z",
        "EndTime": "2023-09-06T14:37:00Z",
        "Status": "completed",
        "ElasticSearchDocID": "doc-67890"
      },
      "ContextInformation": {
        "PreviousContext": "doc-12345",
        "CurrentContext": "Textual context data for current context taken from Context Store..."
      }
    }
    // more SubTasks here
  ],
  "ExecutionOrder": [1, 2], // you could add more subtask IDs here,
  "CreatedAt": "2023-09-06T12:34:56Z",
  "CreatedBy": "username_here",
  "LastUpdated": "2023-09-06T14:37:00Z",
  "LastUpdatedBy": "another_username_here"
}

````


# Guardrails of **G**enerative **P**re-trained **T**ransformers (GPT)
Regarding the risks/guardrails of generative pre-trained Transformers, here are some key points to consider: 

1. **Bias**: LLM models can be biased towards certain groups or perspectives, which can lead to unfair or inaccurate responses. To mitigate this risk, it is important to carefully select and curate the training data used to fine-tune the model, and to test the model on a diverse set of inputs.
1. **Misinformation**: LLM models can generate responses that are factually incorrect or misleading. To mitigate this risk, it is important to verify the accuracy of the responses generated by the model, and to provide users with additional sources of information.
1. **Security**: LLM models can be vulnerable to attacks, such as adversarial attacks or data poisoning attacks. To mitigate this risk, it is important to implement robust security measures, such as data filtering and rate limiting, and to monitor the system for suspicious activity.
1. **Privacy**: LLM models can potentially reveal sensitive information about users, such as their location or personal preferences. To mitigate this risk, it is important to implement strong data protection measures, such as data encryption and access controls, and to obtain user consent for data collection and use.
1. **Ethical considerations**: LLM models can raise ethical concerns, such as the potential for misuse or unintended consequences. To mitigate this risk, it is important to consider the potential impact of the model on different stakeholders, and to implement appropriate safeguards and governance structures. Overall, the risks/guardrails of generative pre-trained Transformers involve issues related to bias, misinformation, security, privacy, and ethical considerations. By carefully considering these risks and implementing appropriate safeguards, it is possible to leverage LLM models in a responsible and effective way.

#### Guardrails During Training:

1. **Data Filtering**: Training data may be screened to remove harmful or misleading content. However, due to the scale of data, this is often imperfect.
  
2. **Training Objectives**: Additional loss terms can be added to steer the model towards desirable behavior, such as discouraging the generation of harmful or misleading content.

3. **Fine-Tuning**: Models are often fine-tuned on a narrower dataset with specific guidelines to make them more useful and safer in specific applications.

#### During Deployment:

1. **Output Filtering**: Before the generated text is shown to the user, it can be screened and possibly modified or blocked if it contains unsafe content.

2. **Rate Limiting**: Limiting the frequency or types of queries to prevent misuse.

3. **User Feedback Loop**: Allowing users to flag problematic outputs to improve the model iteratively.

4. **Monitoring and Auditing**: Continuous monitoring of the model's output for compliance with safety and ethical guidelines.

5. **Human-in-the-Loop**: For sensitive applications, a human can review and approve the model's output before it is delivered to the end-user.

#### Guardrails During Interaction:

1. **Context Awareness**: Offering the user an opportunity to provide more context or clarify ambiguous queries for better and safer responses.

2. **Clarification Prompts**: If a query can potentially lead to harmful or misleading information, the model may ask for clarification.

### Why Guardrails are Important

1. **Safety**: To minimize harmful or misleading information.
  
2. **Ethical Considerations**: To ensure that the model’s behavior aligns with social norms and ethical guidelines.

3. **Legal Compliance**: To adhere to regulations like data protection laws, hate speech laws, etc.

4. **User Experience**: To make the AI system more useful and reliable.

Guardrails are a subject of ongoing research and development, as there is a constant need to balance the capabilities of generative models with the imperatives of safety, ethics, and law.

# Benefits vs Risks Balance
The advent of advanced generative AI models like GPT-3 and GPT-4 has opened new possibilities for human-computer interaction, automation, and data analysis. However, the same capabilities that make these models so powerful also present potential risks if not managed appropriately. Organizations that deploy generative AI models without implementing robust AI safety principles may expose themselves to various forms of abuse and risk related to lack of monitoring of prompting. Below are some of these concerns:

**Abuses:**

1. **Disinformation and Fake News**: Malicious actors could craft prompts that generate fake news or disinformation, which can then be disseminated widely.
1. **Hate Speech and Extremism**: Without proper monitoring, uncensored generative AI sys can be prompted to generate hate speech, extremist ideologies, or other forms of harmful content.
1. **Identity Theft and Fraud**: It's possible to craft prompts that would generate realistic-sounding phishing emails or fraudulent messages.
1. **Manipulation and Bias**: The AI model can be used to generate content that is biased or designed to manipulate public opinion in an unethical way.
1. **Intellectual Property Theft**: Someone could prompt the AI to generate code, art, or literature that closely mimics copyrighted or patented material.
1. **Automated Scams**: Scammers could use the AI to automate the generation of scam emails, messages, or even entire websites that look legitimate.
1. **Child Safety**: The AI could be used to generate inappropriate or harmful content targeted at minors.
1. **Deepfakes**: Generative AI can be used to create deepfake videos or audio recordings that can be used for blackmail, disinformation, or impersonation.

**Risks:**

1. **Legal Risks**: Generating content that is harmful, defamatory, or violates copyright laws could expose an organization to legal action.
1. **Reputational Damage**: Being associated with any form of abuse can severely damage an organization's reputation.
1. **Loss of Public Trust**: Misuse of AI can erode the public's trust not just in the organization but in AI technology as a whole.
1. **Ethical Risks**: Failure to properly monitor AI usage could lead to ethical lapses, such as discrimination or bias.
1. **Operational Risks**: Without proper controls, the AI system could generate outputs that lead to faulty decision-making or operational failures.
1. **Data Security Risks**: Poorly managed AI systems could be a potential point of vulnerability for data breaches.
1. **Economic Risks**: Financial losses could occur if the AI is used for fraudulent activities.
1. **Regulatory Risks**: Lack of compliance with AI ethics guidelines and regulations can result in fines and sanctions.
1. **Global Risks**: On a larger scale, unmonitored and abused AI technologies can have global implications, such as influencing elections or international relations.

For these reasons, it's crucial for organizations to implement AI safety principles, including robust monitoring of the prompts and outputs, to mitigate the risks and prevent abuse.


                """)

def page_6():
    st.markdown("""
                # Chain of Thought
Prompt engineering, in the context of models like OpenAI's GPT series, refers to the craft of designing and refining input prompts to produce desired outputs from the model. While not a direct analog to human memory, it can be used to guide the model towards specific types of responses or to extract particular kinds of knowledge.

When thinking about designing a concept or representing a chain of human memory, one might envision a series of prompts that guide the model through a thought process or exploration of a concept, similar to how a human might recall or learn information step-by-step.

Here's a general approach using the analogy of a human memory chain:

* __Priming the Memory (Foundation):__ Start with broad, foundational questions. This sets the context and ensures that the model accesses the right "part" of its training data. Example: "What is photosynthesis?"
* __Recalling Specific Details (Details):__ Dive deeper into specific elements of the concept, drawing out details and nuances. Example: "Describe the role of chlorophyll in photosynthesis."
* __Application (Synthesis):__ Ask the model to apply the concept in a practical or novel way, synthesizing information from earlier prompts. Example: "How might photosynthesis be used to design sustainable cities?"
* __Reflection and Analysis (Critical Thinking):__ Challenge the model to reflect on or critically analyze the concept. This might involve comparing it to other concepts, evaluating its importance, or discussing its implications. Example: "Compare the energy conversion process in photosynthesis to that in solar panels."
* __Expansion and Exploration (Creativity):__ Encourage the model to think outside the box, exploring potential innovations or future directions related to the concept.Example: "Imagine a world where plants have evolved a more efficient version of photosynthesis. What might that world look like?"

By designing prompts in this way, you are essentially guiding the model through a chain of thought that mirrors how humans might recall, learn, and engage with a concept. This process can be iterative, with outputs from one prompt feeding into the design of the next, allowing for dynamic and adaptive exploration of a topic.

Remember, though, that while the model can generate highly detailed and coherent responses, it doesn't "learn" or "remember" in the same way humans do. Each response is generated based on patterns in its training data, without a true understanding or internal representation of the concept.
                """)

# Create a dictionary of pages
pages = {
    "Page 1": page_1,
    "Page 2": page_2,
    "Page 3": page_3,
    "Page 4": page_4,
    "Page 5": page_5,
    "Page 6": page_6
}

# Create a top menu using buttons as tabs
st.header('')

# Initialize selected_page to "Page 1" as default
selected_page = "Page 1"

# Layout for tabs
col1, col2, col3, col4, col5, col6 = st.columns(6)

# Use the column layout to place buttons
with col1:
    if st.button("This Application"):
        selected_page = "Page 1"

with col2:
    if st.button("Multi-Tenant Arch."):
        selected_page = "Page 2"

with col3:
    if st.button("Single-User APP"):
        selected_page = "Page 3"
        
with col4:
    if st.button("Prompt Design"):
        selected_page = "Page 4"
        
with col5:
    if st.button("Augmenting Skills"):
        selected_page = "Page 5"

with col6:
    if st.button("Chain Of Thought"):
        selected_page = "Page 6"

# Display the selected page
if 'selected_page' in locals():
    pages[selected_page]()