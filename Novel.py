
#Q>
# from langchain import docstore
# class VortexQuery:
#     def __init__(self):
#         load_dotenv()
#         self.chain = self.make_chain()
#         self.chat_history = []

#     def make_chain(self):
#         model = ChatOpenAI(
#             client=None,
#             model="gpt-3.5-turbo",
#             temperature=0,
#         )
#         embedding = OpenAIEmbeddings(client=None)

#         vector_store = Chroma(
#             collection_name=COLLECTION_NAME,
#             embedding_function=embedding,
#             persist_directory=PERSIST_DIRECTORY,
#         )

#         return ConversationalRetrievalChain.from_llm(
#             model,
#             retriever=vector_store.as_retriever(),
#             return_source_documents=True,
#         )

#     def ask_question(self, question: str):
#         response = self.chain({"question": question, "chat_history": self.chat_history})

#         answer = response["answer"]
#         source = response["source_documents"]
#         self.chat_history.append(HumanMessage(content=question))
#         self.chat_history.append(AIMessage(content=answer))

#         return answer, source

# Q2
# from langchain import OpenAI
# import openai
# import pandas as pd
# import numpy as np
# import pickle
# from transformers import GPT2TokenizerFast
# from typing import List

# openai.api_key = "YOUR-API-KEY"
# COMPLETIONS_MODEL = "text-davinci-003"

'''resp = OpenAIBot.__openai_instance__.Completion.create(model="text-davinci-003",
                        prompt=prompt,
                        temperature=0.9,
                        max_tokens=250,
                        top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0.6,
                        user=botRequest.senderId,
                        stop=[" Human:", " AI:"]
                    )'''

# Q.2 example.2
# prompt = "Who won the 2020 Summer Olympics men's high jump?"

# openai.Completion.create(
#     prompt=prompt,
#     temperature=0,
#     max_tokens=300,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0,
#     model=COMPLETIONS_MODEL
# )["choices"][0]["text"].strip(" \n")


# Q.2. 2
# import os
# import time # optional 
# import pandas as pd
# import numpy as np
# import openai
# from openai.embeddings_utils import get_embedding, cosine_similarity
# from transformers import GPT2TokenizerFast
# import matplotlib
# import matplotlib.pyplot as plt
# from sklearn.cluster import KMeans
# import pinecone # for vector database
# rev_per_cluster = 3
# for i in range(n_clusters):
#     print(f"Cluster {i} Theme:", end=" ")

#     reviews = "\n".join(
#         df[df.Cluster == i]
#         .combined.str.replace("Title: ", "")
#         .str.replace("\n\nContent: ", ":  ")
#         .sample(rev_per_cluster, random_state=42)
#         .values
#     )
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=f'What do the following customer reviews have in common?\n\nCustomer reviews:\n"""\n{reviews}\n"""\n\nTheme:',
#         temperature=0,
#         max_tokens=64,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0,
#     )
#     print(response["choices"][0]["text"].replace("\n", ""))

#     sample_cluster_rows = df[df.Cluster == i].sample(rev_per_cluster, random_state=42)
#     for j in range(rev_per_cluster):
#         print(sample_cluster_rows.Score.values[j], end=", ")
#         print(sample_cluster_rows.Summary.values[j], end=":   ")
#         print(sample_cluster_rows.Text.str[:70].values[j])

#     print("-" * 100)

#.2.3
# from langchain import OpenAI
# openai.api_key = "YOUR-API-KEY"
 
# document_list = ["Google was founded in 1998 by Larry Page and Sergey Brin while they were Ph.D. students at Stanford University in California. Together they own about 14 percent of its shares and control 56 percent of the stockholder voting power through supervoting stock. They incorporated Google as a privately held company on September 4, 1998. An initial public offering (IPO) took place on August 19, 2004, and Google moved to its headquarters in Mountain View, California, nicknamed the Googleplex. In August 2015, Google announced plans to reorganize its various interests as a conglomerate called Alphabet Inc. Google is Alphabet's leading subsidiary and will continue to be the umbrella company for Alphabet's Internet interests. Sundar Pichai was appointed CEO of Google, replacing Larry Page who became the CEO of Alphabet.",
# "Amazon is an American multinational technology company based in Seattle, Washington, which focuses on e-commerce, cloud computing, digital streaming, and artificial intelligence. It is one of the Big Five companies in the U.S. information technology industry, along with Google, Apple, Microsoft, and Facebook. The company has been referred to as 'one of the most influential economic and cultural forces in the world', as well as the world's most valuable brand. Jeff Bezos founded Amazon from his garage in Bellevue, Washington on July 5, 1994. It started as an online marketplace for books but expanded to sell electronics, software, video games, apparel, furniture, food, toys, and jewelry. In 2015, Amazon surpassed Walmart as the most valuable retailer in the United States by market capitalization."]
 
# response = openai.Answer.create(
#  search_model="ada",
#  model="curie",
#  question="when was google founded?",
#  documents=document_list,
#  examples_context="In 2017, U.S. life expectancy was 78.6 years.",
#  examples=[["What is human life expectancy in the United States?","78 years."]],
#  max_tokens=10,
#  stop=["\n", "<|endoftext|>"],
# )
 
# print(response)
