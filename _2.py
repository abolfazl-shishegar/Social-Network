import pandas as pd
import networkx as nx

# خواندن فایل CSV
file_path = 'twitter_dataset_8got.csv'
df = pd.read_csv(file_path)

# ساخت گراف جهت‌دار
G = nx.DiGraph()

# افزودن یال‌ها به گراف بر اساس اطلاعات کاربران
for index, row in df.iterrows():
    source_user_id = row['user_id']
    target_user_id = row['mentions_user_id']

    if not pd.isnull(target_user_id):
        G.add_edge(source_user_id, target_user_id)

# محاسبه معیارهای اهمیت و مرکزیت
degree_centrality = nx.degree_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)

# گره‌های با اهمیت بالا (بر اساس معیارها)
important_nodes_degree = sorted(
    degree_centrality, key=degree_centrality.get, reverse=True)[:5]
important_nodes_closeness = sorted(
    closeness_centrality, key=closeness_centrality.get, reverse=True)[:5]
important_nodes_betweenness = sorted(
    betweenness_centrality, key=betweenness_centrality.get, reverse=True)[:5]

# چاپ نتایج با اضافه کردن نام کاربر به کنار user_id
print("Top 5 nodes based on Degree Centrality:")
for node in important_nodes_degree:
    user_id = node
    name = df[df['user_id'] == user_id]['name'].values
    if len(name) > 0:
        name = name[0]
        print(f"User ID: {user_id}, Name: {name}")

print("\nTop 5 nodes based on Closeness Centrality:")
for node in important_nodes_closeness:
    user_id = node
    name = df[df['user_id'] == user_id]['name'].values
    if len(name) > 0:
        name = name[0]
        print(f"User ID: {user_id}, Name: {name}")

print("\nTop 5 nodes based on Betweenness Centrality:")
for node in important_nodes_betweenness:
    user_id = node
    name = df[df['user_id'] == user_id]['name'].values
    if len(name) > 0:
        name = name[0]
        print(f"User ID: {user_id}, Name: {name}")
