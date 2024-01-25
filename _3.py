import pandas as pd
#import nltk
#nltk.download('punkt')
#nltk.download('vader_lexicon')
from nltk import FreqDist
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer

# خواندن دیتاست
file_path = 'twitter_dataset_8got.csv'
df = pd.read_csv(file_path)

# انتخاب فیلد متن
text_field = 'text'
texts = df[text_field]

# توکن‌های متن را استخراج کنید
all_words = []
for text in texts.dropna():
    all_words.extend(word_tokenize(text))

# محاسبه فراوانی کلمات
word_freq = FreqDist(all_words)

# 25 مورد از کلمات کلیدی و پرکاربرد
top_keywords = word_freq.most_common(25)
print("Top 25 Keywords:")
for keyword, freq in top_keywords:
    print(f"{keyword}: {freq}")

# تحلیل مثبت و منفی
sia = SentimentIntensityAnalyzer()
positive_count = 0
negative_count = 0

for text in texts.dropna():
    sentiment_score = sia.polarity_scores(text)['compound']
    if sentiment_score >= 0.05:
        positive_count += 1
    elif sentiment_score <= -0.05:
        negative_count += 1

total_texts = len(texts.dropna())
positive_percentage = (positive_count / total_texts) * 100
negative_percentage = (negative_count / total_texts) * 100

print(f"\nPositive Percentage: {positive_percentage}%")
print(f"Negative Percentage: {negative_percentage}%")

