# Monorepo: Streamlit Applications

## Overview

This monorepo contains three independent **Python school projects** built using **Streamlit**. Each project focuses on a different aspect of data processing, visualization, or machine learning, providing interactive and user-friendly web applications.

## Project 1: Information Retrieval System
### Description
This project implements an **Information Retrieval System** on a medical corpus (**NFCorpus**), improving upon **BM25** as a baseline. The goal is to develop a more effective search engine by leveraging different text-processing techniques.

### Features
- Preprocessing techniques to refine document representation
- Word embeddings with **Word2Vec** for semantic similarity
- Evaluation against **BM25** using **nDCG@5**
- Interactive visualization with **Streamlit**

## Project 2: Restaurant Information Retrieval
### Description
This project allows users to search for restaurants using **scraped data from OpenTable** (scraping did in the WebScraping-Restaurants repository: https://github.com/AurelieMrtn/WebScraping-Restaurants). The application enables users to filter restaurants by **price range** and **cuisine type**.

### Features
- Search restaurants by **name, price, or cuisine**.
- Retrieve a **restaurant summary** based on its name.
- Extract insights from **restaurant reviews**.
- **Ask questions** to find the best matching restaurant.

## TD 1: Document Processing Toolkit
### Description
This project provides various **text-processing utilities** to manipulate documents efficiently. Users can apply different transformations and similarity measurements.

### Features
- **Text Cleaning & Tokenization**
  - Convert to lowercase
  - Remove stop words
  - Remove punctuation
  - Trim extra white spaces
  - Tokenization (**Word, Whitespace, Treebank, WordPunct, Spacy**)

- **Stemming & Lemmatization**
  - PorterStemmer
  - LancasterStemmer
  - SnowballStemmer
  - Lemmatization

- **Text Similarity Metrics**
  - Cosine Similarity
  - Levenshtein Distance
  - Jaccard Distance
  - Q-Grams (Jaccard on n-grams)

- **Statistical Analysis**
  - Zipf’s Law Verification


