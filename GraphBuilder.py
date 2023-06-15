import networkx as nx

class GraphBuilder:
    def __init__(self):
        self.G = nx.Graph()

    def build_graph(self, sentences, sentiments, keyphrases):
        for i, sentence in enumerate(sentences):
            self.G.add_node(i, text=sentence, keyphrases=keyphrases[i], sentiment=sentiments[i])

        for source_node in self.G.nodes():
            for target_node in self.G.nodes():
                if source_node != target_node:
                    source_sentiment = self.G.nodes[source_node]['sentiment']
                    target_sentiment = self.G.nodes[target_node]['sentiment']
                    if (
                        source_sentiment['compound'] >= 0.05 and target_sentiment['compound'] >= 0.05
                    ):
                        edge_label = f"Positive ({source_sentiment['compound']:.2f})"
                    elif (
                        source_sentiment['compound'] <= -0.05 and target_sentiment['compound'] <= -0.05
                    ):
                        edge_label = f"Negative ({source_sentiment['compound']:.2f})"
                    elif (
                        -0.05 < source_sentiment['compound'] < 0.05 and -0.05 < target_sentiment['compound'] < 0.05
                    ):
                        edge_label = f"Neutral ({source_sentiment['compound']:.2f})"
                    else:
                        edge_label = f"Mixed ({source_sentiment['compound']:.2f})"
                    self.G.add_edge(source_node, target_node, label=edge_label)
        return self.G
