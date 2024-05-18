# Import SmartScraperGraph from scrapegraphai.graphs module
from scrapegraphai.graphs import SmartScraperGraph
#from scrapegraphai.graphs import OmniScraperGraph
import nest_asyncio  # Import nest_asyncio module for asynchronous operations
nest_asyncio.apply()  # Apply nest_asyncio to resolve any issues with asyncio event loop

# Configuration dictionary for the graph
graph_config = {
    "llm": {
        "model": "ollama/llama3",  # Specify the model for the llm
        "temperature": 0,  # Set temperature parameter for llm
        "format": "json",  # Specify the output format as JSON for Ollama
        "base_url": "http://localhost:11434",  # Set the base URL for Ollama
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",  # Specify the model for embeddings
        "base_url": "http://localhost:11434",  # Set the base URL for Ollama
    },
    "verbose": True,  # Enable verbose mode for debugging purposes
}

# Initialize SmartScraperGraph with prompt, source, and configuration
smart_scraper_graph = SmartScraperGraph(
    #prompt="List all the content",  # Set prompt for scraping
    prompt="List me all the projects with their descriptions",
    # Source URL or HTML content to scrape
    source="https://github.com/InsightEdge01",
    #source="https://perinim.github.io/projects",
    
    #
    #source="https://www.msn.com/zh-cn/news/other/%E8%83%A1%E8%90%9D%E5%8D%9C%E7%B4%A0%E6%98%AF%E8%8F%A0%E8%90%9D%E7%9A%8445%E5%80%8D-%E7%83%AD%E9%87%8F%E6%AF%94%E8%8B%B9%E6%9E%9C%E8%BF%98%E4%BD%8E-%E8%BF%99%E7%A7%8D%E6%B0%B4%E6%9E%9C%E7%8E%B0%E5%9C%A8%E5%90%83%E6%AD%A3%E5%A5%BD/ar-BB1miM95?ocid=BingHp01&cvid=f326b11390f04dd2fb4a49160b756320&ei=8",

    config=graph_config  # Pass the graph configuration
)

# Run the SmartScraperGraph and store the result
result = smart_scraper_graph.run()

# Print the result
print(result)

# Prettify the result and display the JSON
import json

output = json.dumps(result, indent=2)  # Convert result to JSON format with indentation

line_list = output.split("\n")  # Split the JSON string into lines

# Print each line of the JSON separately
for line in line_list:
    print(line)


