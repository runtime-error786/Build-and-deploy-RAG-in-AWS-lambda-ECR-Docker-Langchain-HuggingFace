from setuptools import find_packages,setup

setup(
    name="QA_System",
    version="0.0.1",
    author="Mustafa Rizwan",
    author_email="mustafa782a@gmail.com",
    packages=find_packages(),
    install_requires=["langchain","langchainhub","bs4","tiktoken","openai","boto3==1.34.37","langchain_community","chromadb","langchain-groq","awscli","pypdf","faiss-cpu","langchain_aws"],
)
# hei