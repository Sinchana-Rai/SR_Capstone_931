# Sales Intelligence Agent 

## CAP 931 : Prompt Engineering Capstone Project

The Sales Intelligence Agent is an AI-powered application that generates account-level sales intelligence by combining product information, company website research, competitive analysis, corporate strategy, leadership research, and product-to-prospect alignment.<br>
The application uses a multi-agent architecture built with Python, LangChain, Groq, BeautifulSoup, Requests, and Streamlit.<br>
A user provides information about a product and a prospective customer through a Streamlit interface. The application then researches the prospect's public websites, analyzes the information using specialized AI agents, and produces a structured Account Intelligence Report that can be downloaded as a Markdown file.

---
### Project Objective
Sales representatives often need to research a prospective customer before beginning a sales conversation.

This research may require reviewing:

- Company websites
- Corporate strategy
- Business priorities
- Technology initiatives
- Leadership teams
- Competitors
- Potential product fit
- Risks and unknown information

Performing this research manually can be time-consuming.

The goal of this project is to demonstrate how Large Language Models and agent-based workflows can automate portions of the sales research process while clearly separating confirmed information from inferred sales opportunities.

The application transforms basic sales opportunity information into a structured account intelligence report.

---
### Main Features
The application provides the following functionality:
- Dynamic user input through a Streamlit UI
- Company website scraping
- Discovery of useful corporate research pages
- Sales opportunity analysis
- Company research analysis
- Competitive analysis
- Strategy and leadership analysis
- Identification of relevant executives
- Identification of missing information and risks
- Final account intelligence report generation
- Downloadable Markdown report

---
### Technology Stack
The project uses the following technologies.

| Technology    | Purpose                                              |
| ------------- | ---------------------------------------------------- |
| Python        | Core application language                            |
| LangChain     | Prompt chains and LLM workflow orchestration         |
| Groq API      | LLM inference                                        |
| Qwen          | Large Language Model used by the agents              |
| Streamlit     | Web application user interface                       |
| Requests      | Website retrieval                                    |
| BeautifulSoup | HTML parsing and text extraction                     |
| python-dotenv | Environment variable management                      |
| uv            | Python dependency and virtual environment management |
| Git/GitHub    | Version control                                      |

The primary model used during development was: qwen/qwen3.6-27b

The available Groq models were checked before selecting the model.

---

### Model Selection and Justification

The final application uses `qwen/qwen3.6-27b` through Groq.

The model was selected after checking the models available to the
configured Groq account.

Reasons for the selection:

- **Availability:** The model was available to the project's Groq account.
- **Cost:** Groq provides usage suitable for learning and prototyping.
- **Speed:** Groq inference provides responsive execution for an interactive Streamlit prototype.
- **Capability:** The model handled structured sales analysis, company research, leadership extraction, competitive analysis, and report synthesis.
- **Context handling:** It was capable of processing the cleaned web research needed by the agents.

A limitation encountered was Groq's token-per-minute limit. The
application therefore limits research and agent-output size before
the final synthesis step.

---

### System Architecture

```text
USER
 |
 v
Streamlit Interface
 |
 v
Sales Workflow
 |
 v
Sales Agent
 |
 v
Website Scraper
 |
 v
Research Agent
 |
 v
Competitor Agent
 |
 v
Corporate Link Discovery
 |
 v
Multi-Page Corporate Research
 |
 v
Strategy & Leadership Agent
 |
 v
Final Report Agent
 |
 v
Account Intelligence Report
 |
 v
Download Report

Each agent has a specialized responsibility instead of asking a single LLM prompt to perform the entire task.
This makes the workflow easier to test, maintain, and extend.

```
---

### Agent Responsibilities
1. Sales Agent

The Sales Agent analyzes the information entered by the sales representative.

Typical inputs include:
- Product
- Product category
- Prospect company
- Value proposition
- Target customer
- Competitors

Purpose of sales agent is to understand the sales opportunity using the information provided by the user.

---

2. Website Scraper

The website scraper retrieves public website information using: requests and BeautifulSoup.
The scraper removes unnecessary HTML elements including :
script, style, nav, footer, header, noscript

Additional text cleaning removes common website noise such as:
Loading... , Skip to main content, Skip to footer, Sponsored, Homepage, Shop all, Privacy policy. Repeated whitespace is also removed.

This produces cleaner website text before it is sent to an LLM.

---
3. Research Agent

The Research Agent analyzes the prospect's public website.

It identifies information such as:

- Company overview
- Products and services
- Business priorities
- Technology signals
- Digital initiatives
- Potential business needs
- Information relevant to the product being sold

The agent is instructed to distinguish between information directly supported by the website and reasonable inferences.This distinction helps reduce unsupported claims.

---

4. Competitor Agent

The Competitor Agent analyzes the competitors supplied by the user.

The agent evaluates:

- Competitors provided
- Competitive context
- Potential competitive overlap
- Differentiation areas
- Competitor mentions in prospect research
- Missing competitive information

---

5. Strategy and Leadership Agent

The Strategy & Leadership Agent performs deeper corporate research.

It analyzes information from multiple corporate pages and produces:

- Company Strategy
- Strategic Priorities
- Leadership Identified
- Leadership Relevant to the Sales Opportunity
- Executive Statements or Public Signals
- Technology or Data Strategy Signals
- Potential Sales Relevance
- Missing Information
- Sources Used

This agent was added because the consumer-facing company homepage alone often does not contain sufficient information about executives or corporate strategy.

---

6. Final Report Agent

The Final Report Agent combines the outputs from the specialized agents.

It generates a structured Account Intelligence Report containing:

- Account Overview
- Company Strategy
- Key Business and Technology Priorities
- Relevant Leadership
- Competitive Landscape
- Opportunity Alignment
- Key Discovery Questions
- Risks / Unknowns
- Sources

The report is designed to help a salesperson prepare for prospect conversations rather than automatically make a final sales decision.

---

### Project Structure

```text 
Capstone_931/
│
├── app.py
├── settings.py
├── pyproject.toml
├── uv.lock
├── .python-version
├── .env
├── .gitignore
├── README.md
│
├── src/
│   │
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── sales_agent.py
│   │   ├── research_agent.py
│   │   ├── competitor_agent.py
│   │   ├── strategy_leadership_agent.py
│   │   └── final_report_agent.py
│   │
│   ├── prompts/
│   │   ├── __init__.py
│   │   ├── sales_prompt.py
│   │   ├── research_prompt.py
│   │   ├── competitor_prompt.py
│   │   ├── strategy_leadership_prompt.py
│   │   └── final_report_prompt.py
│   │
│   ├── tools/
│   │   ├── __init__.py
│   │   └── webscraper.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   └── output_cleaner.py
│   │
│   └── workflows/
│       ├── __init__.py
│       └── sales_workflow.py
│
└── tests/
    ├── __init__.py
    ├── test_available_models.py
    ├── test_groq_model.py
    ├── test_sales_agent.py
    ├── test_research_agent.py
    ├── test_competitor_agent.py
    ├── test_web_scraper.py
    ├── test_multi_web_scraper.py
    ├── test_link_discovery.py
    ├── test_company_research_data.py
    ├── test_strategy_leadership_agent.py
    ├── test_sales_workflow.py
    └── test_final_report_agent.py

The exact test files may vary depending on the final repository.
```
---

### Environment Setup

Prerequisites for the project.

Install:<br>
- Python
- Git
- uv
- A Groq API account/API key

The project uses uv instead of pip for package and environment management.

---
### Clone the Repository
Clone the repository:<br>
git clone ```<GITHUB-REPOSITORY-URL>```

Move into the project:<br>
```cd Capstone_931```

---

### Install Dependencies Using uv
To add an individual dependency during development:<br>
```uv add package-name```

For example:<br>
```uv add langchain```<br>
```uv add langchain-groq```<br>
```uv add python-dotenv```<br>
```uv add requests```<br>
```uv add beautifulsoup4```<br>
```uv add streamlit```<br>
```uv add pypdf python-docx ```<br>
```uv add reportlab``` <br>

Using uv add updates the project dependency configuration rather than requiring a manually maintained requirements.txt.

---- 

### Groq API Configuration

Create a file named:<br>
```.env```
in the project root.

Add:
```GROQ_API_KEY=your_groq_api_key_here```

Do not commit the .env file to GitHub.

Make sure .gitignore contains:
```.env```
```.venv/```
```__pycache__/```
```*.pyc```

The application loads the API key through environment variables.

Example configuration:<br>

```text
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MODEL_ID = "qwen/qwen3.6-27b"

```
Never hardcode the API key directly inside Python source files.

---
### Running the Application
From the project root, run: <br>
```uv run streamlit run app.py```

Streamlit should start a local server.

Typical Local URL: ```http://localhost:8501```

Open the local URL in a browser.

---

### Using the Application

The UI asks the user to provide:

``` Product Name``` : The product being sold.<br>
Example: ``` Salesforce CRM```

```Company URL``` : The prospect's primary website. <br>
Example: ``` https://www.walmart.com```

```Corporate Website``` : The company's corporate or investor website. <br>
Example: ```https://corporate.walmart.com```

```Product Category``` : <br>
Example: ```CRM Software```

```Competitors``` : Separate multiple competitors using commas. <br>
Example: ```HubSpot, Microsoft Dynamics```

```Value Proposition``` : <br>
Example: ```Helps companies manage customers and sales.```

```Target Customer``` : <br>
Example: ```Chief Sales Officer```

After entering the information, click: ```Generate Intelligence Report``` button.<br>
The application performs the complete research workflow and displays the final report.

---

### Testing Strategy

The application was developed incrementally.
Instead of building the complete workflow immediately, individual components were tested first.

Examples include:

``` test_sales_agent.py```<br>
```test_web_scraper.py```<br>
```test_research_agent.py```<br>
```test_competitor_agent.py```<br>
```test_multi_web_scraper.py```<br>
```test_link_discovery.py```<br>
```test_company_research_data.py```<br>
```test_strategy_leadership_agent.py```<br>
```test_final_report_agent.py```<br>
```test_sales_workflow.py```<br>

Individual tests can be executed using following example commands:

```uv run python -m tests.test_sales_agent```

```uv run python -m tests.test_research_agent```

```uv run python -m tests.test_sales_workflow```

This incremental development approach made it easier to identify errors before integrating components into the complete workflow.

---

### Development Challenges and Solutions

Several problems were encountered during development.

**Challenge 1** – Python Module Import Errors

An early error was: ```ModuleNotFoundError: No module named 'src'```<br>
Running test files directly caused Python package resolution issues. Instead of:```python tests/test_sales_agent.py``` tests were executed as modules from the project root: ``` 
uv run python -m tests.test_sales_agent```.
This allowed Python to correctly resolve the src package.

**Challenge 2** - Groq Token Limit

Increasing the number of research pages produced larger prompts.
This resulted in: 
```APIStatusError: Error code: 413```<br>
```Request too large```

One request attempted approximately 9361 tokens 
against an 8000 TPM limit.

Solution: <br>
Research input sizes were controlled through:
```max_links``` ```max_char_per_page``` ```max_total_characters``` <br>
This was necessary because different companies generate different amounts of website and LLM output.

**Challenge 3** - LLM Reasoning Text Appearing in Output

Some model responses initially included internal-style reasoning markup such as:
```text
<think>
...
</think>
```
This reduced report quality.

Solution: <br>
An output cleaning utility was introduced: ```src/utils/output_cleaner.py```

The cleaner removes unnecessary reasoning artifacts before results are passed to other agents or displayed to users.

**Challenge 4** - Hardcoded Streamlit Values

The first Streamlit implementation used default values. 
Although useful during development, this made the application appear specific to the original test scenario.

Solution: <br>
The default values were removed. 
The UI now accepts dynamic user input for:
- Product
- Company
- Corporate Website
- Product Category
- Competitors
- Value Proposition
- Target Customer

---

### Strengths of the Application

**Modular multi-agent design**  : Each agent has a specific responsibility, making the application easier to maintain and improve.

**Dynamic inputs** :The application is not restricted to a single product or prospect.

**Real company research** : The system retrieves current public website information rather than relying entirely on LLM knowledge.

**Corporate link discovery** : The application automatically discovers useful research pages.

**Source-aware analysis** : Prompts encourage the model to distinguish confirmed facts from inferred opportunities.

**Sales-oriented output** : The report translates public company information into:
- Potential opportunity alignment
- Relevant leadership
- Competitive considerations
- Discovery questions
- Risks and unknowns

**User-friendly interface** : Streamlit provides a simple browser interface that does not require users to execute Python manually.

**Downloadable results** : Generated reports can be downloaded for later use.

---

### Security Considerations

The Groq API key should never be committed to GitHub.

Store secrets in: ```.env``` and include: ```.env``` inside ```.gitignore```.

If an API key is accidentally committed to a public repository, revoke the key and generate a new one.

---

### Project Outcome

The project successfully demonstrates how prompt engineering, web research, LLMs, and a multi-agent workflow can be combined to create a practical sales intelligence application.

The final system can:

1. Accept a sales opportunity dynamically.
2. Research public company information.
3. Discover useful corporate research pages.
4. Analyze corporate strategy and leadership.
5. Evaluate competitive context.
6. Connect company priorities with a proposed product.
7. Identify missing information.
8. Generate relevant sales discovery questions.
9. Produce a structured Account Intelligence Report.
10. Allow the report to be downloaded through a browser-based UI.

---

