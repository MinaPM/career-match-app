from transformers import BertTokenizer, BertModel
import torch

# Load pre-trained model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Sample text
job_description = "Looking for a software developer with experience in network security, network and security attacks, firewalls, and other attack tools."
course_description = "This course is designed for Computer Science and Information Technology students. They must have a networking course before taking CS 357. IT students take IT 420 and Computer Science students take CS 356. This course offers an in-depth study of network security issues, types of computer and network attacks, and effective defenses. It provides both a theoretical foundation in the area of security and hands-on experience with various attack tools, firewalls, and intrusion-detection systems. Topics include: network scanning, TCP/IP stack fingerprinting, system vulnerability analysis, buffer overflows, password cracking, session hijacking, denial-of-service attacks, intrusion detection."

# Tokenize and encode
inputs_job = tokenizer(job_description, return_tensors='pt')
inputs_course = tokenizer(course_description, return_tensors='pt')

# Get embeddings
with torch.no_grad():
    job_embedding = model(**inputs_job).last_hidden_state[:, 0, :]  # [CLS] token embedding
    course_embedding = model(**inputs_course).last_hidden_state[:, 0, :]

# Convert to numpy array if needed
job_embedding_np = job_embedding.numpy()
course_embedding_np = course_embedding.numpy()

from sklearn.metrics.pairwise import cosine_similarity

# Calculate cosine similarity
similarity_score = cosine_similarity(job_embedding_np, course_embedding_np)
print(f"Similarity Score: {similarity_score[0][0]}")