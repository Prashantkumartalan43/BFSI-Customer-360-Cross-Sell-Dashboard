# BFSI-Customer-360-Cross-Sell-Dashboard

This project mimics a real-world BFSI analytics workflow used in retail banking and fintech organizations.

[Streamlit Dashboard link](https://bfsi-customer-360-cross-sell-dashboard-nurnfav9fj7oxrno4nqbhu.streamlit.app/)

## Project Overview

Banks and financial institutions often struggle to maximize customer lifetime value due to fragmented data, limited behavioral segmentation, and generic cross-sell campaigns.

This project builds a Customer 360 analytics pipeline using Python and Machine Learning to:

* Integrate multi-dimensional customer data

* Segment customers into actionable personas using clustering

* Identify product penetration gaps

* Generate personalized cross-sell recommendations

* Visualize insights through an interactive dashboard

The solution mimics a real-world BFSI analytics workflow used in retail banking and fintech organizations.

## Business Objectives

* Create a unified Customer 360 view combining demographic, financial, and behavioral attributes.

* Identify distinct customer segments using unsupervised learning.

* Quantify product penetration and cross-sell opportunities by segment.

* Recommend targeted products for each customer.

* Provide an interactive dashboard for business stakeholders.

## Dataset Description

The dataset contains 3,000 synthetic retail banking customers with the following feature groups:

### Customer Profile

1. Age

2. Income

3. Tenure

4. Risk Score

### Financial Behavior

1. Average Balance

2. EMI to Income Ratio

3. Spend to Income Ratio

4. Credit Utilization

5. Transaction Activity Score

### Digital Engagement

1. App usage score

2. Online transaction frequency

### Product Holdings

1. Credit Card

2. Loan

3. Investments

## Feature Engineering

Key engineered features:

* Financial Ratios

1. EMI / Income

2. Spend / Income

3. Credit Utilization

4. Engagement Indicators

5. Transaction activity score

6. Digital engagement index

7. Product Indicators

8. Binary ownership flags for each product


## Modeling Approach
Clustering Algorithm

* K-Means Clustering

Model Selection

Evaluated K from 2 to 8 using Silhouette Score

Best result observed at:

```K = 3 (Silhouette ≈ 0.126)```

### Final Segments Identified
Segment	Description
1. Mass Retail / Low Engagement	Low product penetration, basic banking customers
2. Credit Active Middle Segment	High loan and credit usage
3. Affluent & Investment Ready	High income, high balances, investment-ready

## Segment Distribution

| Segment | % of Customers | Description |
|---------|----------------|-------------|
| Mass Retail / Low Engagement | 49% | Low product holding, basic banking users |
| Credit Active Middle Segment | 24% | High loan utilization customers |
| Affluent & Investment Ready | 27% | High income and investment ready |



## Product Penetration Insights

| Segment | Credit Card | Loan | Investments |
|---------|-------------|------|-------------|
| Affluent | 98% | 51% | 53% |
| Credit Active | 65% | 79% | 50% |
| Mass Retail | 35% | 33% | 30% |

Key Insights known from this:

* Affluent customers are saturated on cards but underpenetrated on investments.

* Credit-active customers present strong refinancing and upsell potential.

* Mass retail customers offer large base for entry-level product growth.

## Cross-Sell Recommendation Logic

Each customer receives a rule-based recommendation aligned with their segment and product gaps.

Example Logic

Affluent Segment

* Wealth products, premium cards, portfolio upgrades

Credit Active Segment

* Loan top-ups, refinancing, card upgrades

Mass Retail Segment

* Savings, fixed deposits, micro-insurance, starter credit cards


## Streamlit Dashboard

An interactive Streamlit dashboard provides:

* Segment distribution visualization

* Product penetration by segment

* Cross-sell campaign mix

* Customer-level lookup

* Filter-driven analytics

Run `streamlit run app.py` to launch the dashboard

Screenshots:

1.
<img width="1919" height="770" alt="image" src="https://github.com/user-attachments/assets/c264618c-f8ef-48d3-aae6-e4b4ba4245ff" />

2.
<img width="1917" height="558" alt="image" src="https://github.com/user-attachments/assets/8eb0a30c-58f6-4c51-87ab-49ade43bcc8e" />




