import pickle
import spacy
import pandas as pd
from time import time

# Abrir arquivo com dataset
dataset = pd.read_csv("stack_exchange_clean.csv")
print("Dataset opened")

nlp = spacy.load('en_core_web_lg')
print("Language model loaded")

with open("nlp_data.pkl", "rb") as f:
	doc_dataset = pickle.load(f)

print("NLP Data loaded")
# doc_dataset = []
# for enum_i, (index, row) in enumerate(dataset.iterrows()):
# 	# print("\r {}/{}             ".format(enum_i, len(dataset)), end="")
# 	doc_dataset.append(nlp("{} {} {}".format(row["title"], row["body"], row["answer"])))
# doc_dataset = [nlp("{} {} {}".format(row["title"], row["body"], row["answer"])) for index, row in dataset.iterrows()]
# doc_dataset = [nlp("{} {} {}".format(sample["question"], sample["body"], sample["answer"])) for sample in dataset]
# print("Dataset loaded")

needle = 34
num_threads = 20
thread_ans = [-1]*num_threads

def worker(i, h):
	"""thread worker function"""
	max_idx = -1
	max_similarity = -float("inf")
	for i, doc in enumerate(h):
			current_similarity = doc_query.similarity(doc)
			if v:
				print("#{} - sim = {}".format(i, current_similarity))
			if current_similarity > max_similarity:
				if v:
					print("new best")
				max_similarity = current_similarity
				max_idx = i
	thread_ans[i] = (best, best_diff)
	print(best)
	return best

def best_match(query, v=False):
	start = time()
	doc_query = nlp(query)

	max_idx = -1
	max_similarity = -float("inf")

	for i, doc in enumerate(doc_dataset):
			current_similarity = doc_query.similarity(doc)
			if v:
				print("#{} - sim = {}".format(i, current_similarity))
			if current_similarity > max_similarity:
				if v:
					print("new best")
				max_similarity = current_similarity
				max_idx = i
	end = time()
	print("It took {}s to find you an answer.".format(end - start))
	print("Best index:", max_idx)
	best_df = dataset.iloc[max_idx]
	# question_obj["question"], question_obj["body"], question_obj["answer"]
	final_obj = {
		"question": best_df["title"],
		"body": best_df["body"],
		"answer": best_df["answer"] if best_df["answer"] != "Wigitijangs" else "[No answer available]"
	}
	return final_obj

def best_match_p(query, v=False):
	start = time()
	doc_query = nlp(query)

	max_idx = -1
	max_similarity = -float("inf")

	for i, doc in enumerate(doc_dataset):
			current_similarity = doc_query.similarity(doc)
			if v:
				print("#{} - sim = {}".format(i, current_similarity))
			if current_similarity > max_similarity:
				if v:
					print("new best")
				max_similarity = current_similarity
				max_idx = i
	end = time()
	print("It took {}s to find you an answer.".format(end - start))
	print("Best index:", max_idx)
	best_df = dataset.iloc[max_idx]
	# question_obj["question"], question_obj["body"], question_obj["answer"]
	final_obj = {
		"question": best_df["title"],
		"body": best_df["body"],
		"answer": best_df["answer"] if best_df["answer"] != "Wigitijangs" else "[No answer available]"
	}
	return final_obj

if __name__ == "__main__":
	print("Start")
	while True:
		print("$ ", end="")
		query = input()
		if query == "q":
			exit(0)
		# Carrega o tokenizer, tagger, parser, REN (Reconhecedor de Entidades Nomeadas) e word embeddings da língua inglesa.
		best = best_match(query)

		print("Best match")
		print("Title:", best["question"])
		print("Body:", best["body"])
		print("Answer:", best["answer"])
