import matplotlib.pyplot as plt
from TextAnalyzer import TextAnalyzer
from GraphBuilder import GraphBuilder

corpus = """I had a wonderful day at the beach with my friends. The weather was perfect, and we enjoyed swimming and playing beach volleyball. It was a day filled with laughter and joy.
          Today, I went grocery shopping and ran some errands. The store had all the items I needed, and I was able to check off everything on my to-do list. It was a typical day without any remarkable experiences.
          I received disappointing news today. I didn't get the job I interviewed for, and it left me feeling discouraged and frustrated. I had put in a lot of effort and had high hopes for this opportunity. It's disheartening to receive a rejection.
          """

text_analyzer = TextAnalyzer(corpus)
sentiments = text_analyzer.analyze_sentiments()
keyphrases = text_analyzer.extract_keyphrases()
sentences = [sentence.text for sentence in text_analyzer.nlp(corpus).sents]

graph_builder = GraphBuilder()
G = graph_builder.build_graph(sentences, sentiments, keyphrases)

plt.figure(figsize=(24, 16))
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx(G, pos=pos, with_labels=True, node_size=3000, font_size=10) 
node_labels = nx.get_node_attributes(G, 'keyphrases')
nx.draw_networkx_labels(
    G, pos=pos, labels=node_labels, font_size=10, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.2')
)
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels, font_size=10, label_pos=0.3)
plt.title('Sentiment Analysis Graph')
plt.axis('off')
plt.show()
