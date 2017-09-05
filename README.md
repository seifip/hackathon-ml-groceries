# HackerEarth Deep Learning Challenge #1
### Identify grocery category

Brief: https://www.hackerearth.com/challenge/competitive/deep-learning-challenge-1/

Dataset: https://he-s3.s3.amazonaws.com/media/hackathon/deep-learning-challenge-1/identify-the-objects/a0409a00-8-dataset_dp.zip

## Problem statement

The applications of Deep Neural Nets is on a roll. Whether it is healthcare, transportation, or retail, companies across all industries are excited about investing in building intelligent solutions. Meanwhile, let’s hope human intelligence remains uncontested.

In this challenge, you will help one of the largest retailers in Germany improve their inventory-management process in its Food and Groceries business. The company is looking for intelligent solutions that can reduce the amount of human effort in its warehouse and retail outlets.

A solution such as a powerful image classifier can help the company track shelf inventory, categorize products, record product volume etc.

You are required to predict the category of each product.

## Solution
Given that the provided groceries dataset shares many similarities with images in the ImageNet dataset, I used a pre-trained InvisionV3 model, adapted with transfer learning and fine tuning.

This led to a prediction score of 0.65777 on the test version of the dataset.
