import pickle
import streamlit as st
import re
import os
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import nltk

# Download NLTK data if not already present
try:
    stopwords.words('english')
except LookupError:
    nltk.download('stopwords')


class SentimentAnalyzer:
    def __init__(self):
        try:
            # Check if model files exist
            if not os.path.exists('Models/model.pkl'):
                st.error("Model file 'Models/model.pkl' not found!")
                st.info("Please ensure your trained model is saved in the Models/ directory")
                st.stop()

            if not os.path.exists('Models/tfidf.pkl'):
                st.error("Vectorizer file 'Models/tfidf.pkl' not found!")
                st.info("Please ensure your TF-IDF vectorizer is saved in the Models/ directory")
                st.stop()

            with open('Models/model.pkl', 'rb') as f:
                self.model = pickle.load(f)
            with open('Models/tfidf.pkl', 'rb') as f:
                self.vectorizer = pickle.load(f)

        except ImportError as e:
            st.error(f"Missing required library: {e}")
            st.info("Please install required packages: pip install scikit-learn nltk streamlit")
            st.stop()
        except Exception as e:
            st.error(f"Error loading models: {e}")
            st.stop()

        self.comment = None
        self.cleaned_comment = None
        self.prediction = None
        self.stopwords = stopwords.words('english')

    def preprocessing(self, comment):
        self.comment = comment
        stopwords_set = set(self.stopwords)
        emoji_pattern = re.compile('(?::|;|=)(?:-)?(?:\)|\(|D|P)')

        # Remove HTML tags
        comment_clean = re.sub('<[^>]*>', '', self.comment)

        # Extract emojis
        emojis = emoji_pattern.findall(self.comment)

        # Clean text and add emojis
        text = re.sub('[\W+]', ' ', comment_clean.lower()) + ' '.join(emojis).replace('-', '')

        # Stemming and stopword removal
        porter = PorterStemmer()
        text = [porter.stem(word) for word in text.split() if word not in stopwords_set]

        self.cleaned_comment = " ".join(text)

    def predict_sentiment(self):
        vector = self.vectorizer.transform([self.cleaned_comment])
        self.prediction = self.model.predict(vector)[0]

    def app(self):
        # Sidebar
        st.sidebar.title("📊 Sentiment Analysis Info")
        st.sidebar.markdown("---")

        st.sidebar.subheader("ℹ️ About")
        st.sidebar.write("""
        This application analyzes the sentiment of text comments using 
        machine learning to classify them as positive or negative.
        """)

        st.sidebar.subheader("🔧 How it works")
        st.sidebar.write("""
        1. **Text Preprocessing**: Removes HTML tags, handles emojis, converts to lowercase
        2. **Stopword Removal**: Removes common words (a, an, the, etc.)
        3. **Stemming**: Reduces words to their root form
        4. **Vectorization**: Converts text to numerical features using TF-IDF
        5. **Prediction**: Uses trained ML model to classify sentiment
        """)

        st.sidebar.subheader("💡 Tips for better results")
        st.sidebar.write("""
        • Write clear, complete sentences
        • Use natural language
        • Include context when possible
        • Avoid excessive abbreviations
        • Mix of adjectives helps accuracy
        """)

        st.sidebar.subheader("📝 Example Comments")
        st.sidebar.markdown("**Positive:**")
        st.sidebar.code("This product is amazing and I love it!")

        st.sidebar.markdown("**Negative:**")
        st.sidebar.code("This is terrible and disappointing.")

        st.sidebar.markdown("---")
        st.sidebar.caption("Built By Muhammad Haseeb Raza")

        # Main app
        st.title("Sentiment Analysis")
        st.subheader("Analyze the sentiment of your text")
        st.markdown("Enter a comment below to determine if it has positive or negative sentiment.")

        comment = st.text_input("Comment", placeholder="Enter your comment here...")

        col1, col2, col3 = st.columns([1, 1, 2])
        with col1:
            button = st.button("Analyze Sentiment")

        if button and comment:
            with st.spinner("Analyzing sentiment..."):
                self.preprocessing(comment)
                self.predict_sentiment()

                if self.prediction == 1:
                    st.success("✅ Positive Sentiment 😊")
                    st.balloons()
                else:
                    st.error("❌ Negative Sentiment 😞")

                # Show processed text in expander
                with st.expander("View Preprocessed Text"):
                    st.write(f"**Original:** {comment}")
                    st.write(f"**Processed:** {self.cleaned_comment}")

        elif button and not comment:
            st.warning("⚠️ Please enter a comment to analyze!")

        # Additional info section


if __name__ == "__main__":
    system = SentimentAnalyzer()
    system.app()