# Score-based Sentiment Analysis Graph
The project aims to analyze the sentiment of individual sentences in a text corpus and represent them as nodes in a graph. Each node is labeled with the sentiment score and contains key phrases extracted from the corresponding sentence. The sentiment scores are computed using the VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analysis tool, which provides sentiment intensity scores for positive, negative, and neutral sentiments.

The text corpus is processed using the spacy library to extract sentences and perform natural language processing tasks. The rake_nltk library is used to extract key phrases from each sentence, which helps in understanding the main topics discussed in the text.

Based on the sentiment scores, the project builds a graph using the networkx library. Each sentence is represented as a node in the graph, and the sentiment relationships between sentences are captured using edges. The edge labels indicate the sentiment relationship (positive, negative, neutral, or mixed) along with the corresponding sentiment score.

Finally, the sentiment analysis graph is visualized using the matplotlib library. The graph layout is generated using the spring layout algorithm provided by networkx. The node labels display the extracted key phrases, and the edge labels indicate the sentiment relationship between the connected nodes.

## Features
- Perform sentiment analysis on a text corpus.
- Extract key phrases from sentences to understand the main topics.
- Build a sentiment analysis graph representing the sentiment relationships between sentences.
- Visualize the sentiment analysis graph with node and edge labels.

## Usages
- Install the required dependencies by running pip install -r requirements.txt.
- Modify the corpus variable in the main.py file to include your desired text corpus.
- Run the main.py file to execute the sentiment analysis and graph visualization.
- The sentiment analysis graph will be displayed, showcasing the sentiment relationships between sentences.

## Example
Here is an example of the sentiment analysis graph generated for a sample text corpus:
![image](https://github.com/ivarrvinter/score-based-sentiment-analysis-graph/assets/109881262/47eb5362-90a6-4ee3-891f-3454c51516d3)

## Credits
The project utilizes the following libraries:
- [SpaCy](https://spacy.io/)
- [NetworkX](https://networkx.org/)
- [Matplotlib](https://matplotlib.org/)
- [Rake_NLTK](https://pypi.org/project/rake-nltk/)

## Disclaimer
The sentiment analysis results provided by this project are based on the VADER sentiment analysis tool. While VADER is widely used and provides reliable sentiment scores, it may not always capture the nuanced sentiment expressed in certain texts. Therefore, the results should be interpreted with caution and further analysis may be required for accurate sentiment understanding.
