# Avito prediction competition

## 数据情况
```text
region: 枚举
city: 枚举
parent_category_name: 枚举
category_name： 枚举
param1: 
param2:
param3:
title: tfidf 方法？
description： tfidf方法？
price： 浮点数，需要归一化
item_seq_number： 
image： 关联image数据
image_top_1： 枚举，图片分类结果

<mark>label</mark>: deal_probability
```

## 衍生字段
> WeekDay - Day of the week when the Ad was activated

> Month - Month when the Ad was activated

> Month Day - Day of the month when the Ad was activated

> Description_len - Total words in the description, ie. the description length

> Title_len - Total words in the title, ie. the title length

> Total Period - total number of days for which the Ad was run

> Deal Class - A binary variable which is 1 when the deal probability is > greater than 0.5 else 0

## 数据情况

## 工作内容



## 预处理的一些代码
```python
## 1. reading 

train_df = pd.read_csv("../input/train.csv", parse_dates=["activation_date"])
pr_train = pd.read_csv("../input/periods_train.csv", parse_dates=["activation_date", "date_from", "date_to"])

## 2. feature engineering 

train_df['weekday'] = train_df.activation_date.dt.weekday
train_df['month'] = train_df.activation_date.dt.month
train_df['day'] = train_df.activation_date.dt.day

train_df['description'] = train_df['description'].fillna(" ")
train_df['description_len'] = train_df['description'].apply(lambda x : len(x.split()))

train_df['title'] = train_df['title'].fillna(" ")
train_df['title_len'] = train_df['title'].apply(lambda x : len(x.split()))

train_df['deal_class'] = train_df['deal_probability'].apply(lambda x: ">=0.5" if x >=0.5 else "<0.5")
pr_train['total_period'] = pr_train['date_to'] - pr_train['date_from']

## 3. FILLNA

```

