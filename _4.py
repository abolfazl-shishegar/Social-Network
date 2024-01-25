import pandas as pd
import matplotlib.pyplot as plt

# خواندن فایل CSV به عنوان DataFrame
file_path = 'C:/Users/Abolfazl/Downloads/Telegram Desktop/sampeled2_gotTwitter.csv'
df = pd.read_csv(file_path)

# تحلیل تعداد فعالیت‌های هر کاربر
user_activity = df['screen_name'].value_counts()

# گرفتن 15 کاربر فعال
top_users = user_activity.head(15)

# نمایش نتایج
print("لیست 15 کاربر فعال:")
print(top_users)

# تحلیل میزان تاثیرگذاری محتوای 15 کاربر بر کل شبکه
total_tweets = df.shape[0]
top_users_tweets = df[df['screen_name'].isin(top_users.index)].shape[0]
impact_percentage = (top_users_tweets / total_tweets) * 100

# نمایش نتایج
print(
    f"\nمیزان تاثیرگذاری محتوای 15 کاربر بر کل شبکه: {impact_percentage:.2f}%")

# تحلیل و نمایش نمودار میزان فعالیت کاربران
plt.figure(figsize=(12, 6))
top_users.plot(kind='bar', color='skyblue')
plt.title('Number of user activities')
plt.xlabel('نام کاربری')
plt.ylabel('Number of activities')
plt.show()
