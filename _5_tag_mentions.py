import pandas as pd
import matplotlib.pyplot as plt

# خواندن داده‌ها از فایل CSV
file_path = 'twitter_dataset_8got.csv'
df = pd.read_csv(file_path)

# تحلیل جامعه‌های فعال بر اساس mentions_screen_name
mentions_communities = df['mentions_screen_name'].str.split(',').explode().str.strip()
mentions_active_communities = mentions_communities.value_counts()

# تحلیل جامعه‌های فعال بر اساس hashtags
hashtags_communities = df['hashtags'].str.split(',').explode().str.strip()
hashtags_active_communities = hashtags_communities.value_counts()

# ترکیب دو تحلیل بر اساس mentions و hashtags
combined_active_communities = mentions_active_communities.add(hashtags_active_communities, fill_value=0)

# نمایش ۱۰ جامعه فعال برتر
top_communities = combined_active_communities.head(10)
print("Top 10 Active Communities:")
print(top_communities)

# رسم نمودار توزیع جامعه‌های فعال
plt.figure(figsize=(10, 6))
top_communities.plot(kind='bar', color='skyblue')
plt.title('Top 10 Active Communities')
plt.xlabel('Screen Name or Hashtags')
plt.ylabel('Number of Occurrences')
plt.show()

