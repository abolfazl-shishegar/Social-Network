import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# خواندن داده‌ها از فایل CSV
file_path = 'twitter_dataset_8got.csv'
df = pd.read_csv(file_path)

# انتخاب فیلدهای متنی برای خوشه‌بندی
text_columns = ['description', 'text']

# ایجاد یک ستون جدید به نام 'combined_text' که ترکیب متن‌های انتخاب شده است
df['combined_text'] = df[text_columns].apply(lambda row: ' '.join(row.dropna()), axis=1)

# استفاده از TF-IDF برای تبدیل متن به بردارهای عددی
tfidf_vectorizer = TfidfVectorizer(max_df=0.85, max_features=5000)
tfidf_matrix = tfidf_vectorizer.fit_transform(df['combined_text'].values.astype('U'))

# استفاده از الگوریتم K-Means برای خوشه‌بندی
num_clusters = 5  # تعداد خوشه‌ها ممکن است تغییر کند
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
df['cluster'] = kmeans.fit_predict(tfidf_matrix)

# اگر نیاز دارید، می‌توانید داده‌ها را در فایل جدیدی ذخیره کنید
df.to_csv('clustered_data.csv', index=False)

# نمایش تعداد اعضای هر خوشه
cluster_sizes = df['cluster'].value_counts()
print("Number of members of each cluster:")
print(cluster_sizes)
