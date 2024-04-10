# Movie Recommender System - NLP Project(Bag of words)

## Overview
This project is based on Content-Based Filtering, which utilizes item metadata such as genre, director, description, actors, etc., for movies to provide recommendations. The underlying principle of these recommender systems is that if a person enjoys a particular item, they are likely to appreciate items similar to it.

## Workflow
1. **Data Collection:** Data was sourced from Kaggle. Following a meticulous selection process, only specific columns were retained while the rest were discarded:
   - `id`
   - `title`
   - `genres`
   - `keywords`
   - `overview`
   - `cast`
   - `crew`

2. **Data Preprocessing:** Textual data underwent preprocessing where they were concatenated into a `tags` column, serving as the foundation for subsequent modeling.

3. **Text Processing:** Tags were subjected to stemming, tokenization, and vectorization (Bag of Words). Distances were computed using Cosine similarity.

4. **Recommender System:** A recommender function was developed to identify movies similar to a given film.

5. **Application Development:** The processed files were pickled and utilized in `app.py` to create an application using Streamlit.

6. **Deployment:** Initially, the application was hosted on Heroku.

By following this workflow, the Movie Recommender System was developed, allowing users to discover movies based on their preferences and similarities.
