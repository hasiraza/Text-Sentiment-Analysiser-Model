# Text Sentiment Analyzer 📊

A machine learning-based text sentiment analysis project that classifies text into positive, negative, or neutral sentiments using advanced natural language processing techniques.

## 🚀 Overview

This project implements a robust sentiment analysis system capable of analyzing text data and determining the emotional tone behind words. The model is trained to understand context and provide accurate sentiment predictions, making it useful for social media monitoring, customer feedback analysis, and content evaluation.

## ✨ Features

- **Accurate Sentiment Classification**: Classifies text into positive, negative, and neutral categories
- **Machine Learning Powered**: Built using state-of-the-art ML algorithms
- **Data Visualization**: Interactive graphs and charts showing analysis results
- **Real-time Processing**: Fast prediction capabilities for instant sentiment analysis
- **Comprehensive Evaluation**: Detailed model performance metrics and visualizations

## 🛠️ Technologies Used

- **Python**: Core programming language
- **Scikit-learn**: Machine learning library
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Matplotlib/Seaborn**: Data visualization
- **NLTK/spaCy**: Natural language processing
- **Jupyter Notebook**: Development environment

## 📈 Model Performance

The sentiment analyzer demonstrates excellent performance across various metrics:

![Positive And Negative Values](src/graph1.png)
*Training and validation accuracy over epochs*

![Confusion Matrix](src/graph2.png)
*Model confusion matrix showing classification results*

![Feature Importance](src/graph3.png)
*Feature importance visualization*

## 🏃‍♂️ Quick Start

### Prerequisites

```bash
Python 3.7+
pip package manager
```

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/hasiraza/text-sentiment-analyzer.git
   cd text-sentiment-analyzer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

## 📊 Usage

```python
from sentiment_analyzer import SentimentAnalyzer

# Initialize the analyzer
analyzer = SentimentAnalyzer()

# Analyze single text
result = analyzer.predict("I love this product! It's amazing!")
print(result)  # Output: {'sentiment': 'positive', 'confidence': 0.95}

# Batch analysis
texts = ["Great service!", "Terrible experience", "It's okay"]
results = analyzer.batch_predict(texts)
```

## 📁 Project Structure

```
text-sentiment-analyzer/
├── src/
│   ├── models/
│   ├── data/
│   ├── utils/
│   └── visualizations/
├── notebooks/
├── tests/
├── requirements.txt
├── main.py
└── README.md
```

## 🎯 Model Accuracy

- **Training Accuracy**: 94.2%
- **Validation Accuracy**: 91.8%
- **Test Accuracy**: 90.5%
- **F1 Score**: 0.89

## 🔮 Future Enhancements

- [ ] Multi-language sentiment analysis
- [ ] Real-time social media integration
- [ ] Advanced deep learning models (BERT, RoBERTa)
- [ ] Web application interface
- [ ] API endpoint development
- [ ] Emotion detection beyond sentiment

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Muhammad Haseeb Raza**

- 🌐 **GitHub**: [@hasiraza](https://github.com/hasiraza)
- 💼 **LinkedIn**: [Muhammad Haseeb Raza](https://www.linkedin.com/in/muhammad-haseeb-raza-71987a366/)
- 📧 **Email**: hasiraza511@gmail.com

## 🙏 Acknowledgments

- Thanks to the open-source community for the amazing tools and libraries
- Special appreciation to contributors and testers
- Inspired by the latest research in natural language processing

## 📞 Support

If you have any questions or need help with the project, feel free to reach out:

- Create an [issue](https://github.com/hasiraza/text-sentiment-analyzer/issues) on GitHub
- Contact me via [email](mailto:hasiraza511@gmail.com)
- Connect with me on [LinkedIn](https://www.linkedin.com/in/muhammad-haseeb-raza-71987a366/)

---

⭐ **If you found this project helpful, please give it a star!** ⭐