# H&M-Product-Recommendations
> Product recommendations based on data from previous transactions, as well as from customer and product meta data

## Background
Nowadays we can see recommender system everywhere and everyday. Since it has a variety of benefits, many companies, regardless of their business type, use a recommender system, and they spend a lot of money and time developing a better algorithms. An accurate recommender system not only increases a company's benefits by raising average order value and the number of items per order, but it also raises customer's satisfactory. In addition, it plays a role as a personalized marketing by making customers come back. With these benefits, a recommender system is not an optional, but must-have function for all companies. There are many different recommender system algorithms, but content-based filtering and collaborative filtering form the foundation of most recommender systems.

## Problem
H&M is a large fashion company with 53 online stores and around 4,850 markets. Its online store provides customers with an a variety of selection of products to browse through. While clothing companies generally want to provide extensive options for consumers, this creates some problems. Too many choices makes customers have difficulty in finding what they are looking for and what interests them quickly. If this phenomenon lasts for a long time, shoppers end up not buying any products from the online store. For this reason, having a recommender system with a high accuracy is an important key to enhance the shopping experience, by extension, the company's profits.

## Data
The dataset we used for this project has been provided by H\&M group. The official name of this dataset is 'H\&M Personalized Fashion Recommendations', and we extracted it from Kaggle.

Data source: https://www.kaggle.com/c/h-and-m-personalized-fashion-recommendations

## Repo Structure
The repo is structured as follows: Notebooks are grouped according to their series (e.g., 10, 20), which reflects the general task to be performed in those notebooks. Start with theh *0 notebook in the series and add other investigations relevant to the task in the series (e.g., `21-content-based-filtering`). 

1* is related to data processing. 2* is about modeling: naive method, content-based filtering, collaborative filtering, and hybrid method.

## Models
Four different algorithms were implemented: Naive method, content-based filtering, collaboriative filtering, and hybrid method. Naive method is to use the top ten most popular products across all customers and recommending those to everyone. While the content-based filtering uses item features to recommend other items similar to what the user likes, collaborative filtering is solely based on the past interactions that have been recorded between users and items, in order to produce new recommendations. Lastly, for naive hybrid recommender system, we extracted top 5 recommendations from the each model we developed previously, and combined them. 

## Results
<img width="234" alt="Screen Shot 2022-05-07 at 7 11 28 AM" src="https://user-images.githubusercontent.com/69788782/167253853-f8b2b76e-60bd-4b70-824e-0f0f4629d23c.png">


## Contact Info
Amanda Konet, Graduate Student
Vanderbilt University Data Science Institute   
amanda.konet@vanderbilt.edu 

Preston Abraham, Graduate Student
Vanderbilt University Data Science Institute   
preston.d.abraham@vanderbilt.edu 

Soyeon Park, Graduate Student
Vanderbilt University Data Science Institute   
soyeon.park@vanderbilt.edu 

