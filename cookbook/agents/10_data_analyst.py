"""
Movie data analysis system using DuckDB

This script implements a data analyst agent that uses DuckDB to analyze IMDB movie data and visualizes the statistics in ASCII art.

Main features:
- Efficient data analysis with DuckDB
- ASCII art display of histograms
- Automatic selection of optimal bucket size
- Detailed description of the analysis process

Installation of required packages:
pip install duckdb
"""

import json

from phi.model.openai import OpenAIChat
from phi.agent.duckdb import DuckDbAgent

# Setting Up a Data Analyst Agent
data_analyst = DuckDbAgent(
    # Using GPT-4 model
    model=OpenAIChat(model="gpt-4o"),
    markdown=True,  # Output in Markdown format
    # Defining the data model
    semantic_model=json.dumps(
        {
            "tables": [
                {
                    "name": "movies",
                    "description": "Dataset of movie information obtained from IMDB, including ratings, release year, genre, etc.",
                    "path": "https://phidata-public.s3.amazonaws.com/demo_data/IMDB-Movie-Data.csv",
                }
            ]
        },
        indent=2,
    ),
    # Instructions to the agent
    instructions=[
        "Clearly explain the reasons for selecting the analysis method",
        "Visualize considering the characteristics of the data",
        "Select a bucket size with statistical significance",
        "Ensure the display is visually intuitive"
    ]
)

# Analyze the distribution of ratings
data_analyst.print_response(
    """
    Create a histogram for movie ratings.
    Select an appropriate bucket size and explain the reason for your choice.
    Display the results in an easy-to-view ASCII art.
    """,
    stream=True  # Display the analysis process in real-time
)
