# Chess Player Data Scraper & Analyzer

## Project Overview

This project provides an end-to-end solution for collecting, processing, and visualizing comprehensive chess player data. It leverages Python for web scraping and data preparation, followed by Power BI for creating an interactive and insightful dashboard. The goal is to provide a clear overview of chess player statistics, including ratings, rankings, and geographical distribution, for various formats (Classical, Rapid, Blitz).

## Features

* **Automated Web Scraping:**
    * Efficiently extracts chess player names, titles (GM, IM, etc.), countries, and their Classical, Rapid, and Blitz ratings from the `chess.com/ratings` platform.
    * Automates navigation through multiple web pages to ensure comprehensive data collection.

* **Data Preparation & Storage:**
    * Performs robust data cleaning and preprocessing to ensure data accuracy and consistency.
    * Utilizes Pandas for structuring and manipulating raw scraped data into a clean, tabular CSV format.

* **Interactive Power BI Dashboard:**
    * [cite_start]**Visualizes key metrics** such as total players, grandmasters, international masters, and their distribution across countries[cite: 1].
    * [cite_start]**Presents detailed player information**, including individual ratings and world/national ranks[cite: 2].
    * [cite_start]**Showcases top 10 players** for Classical, Rapid, and Blitz formats[cite: 3].
    * [cite_start]**Displays national team compositions** and average ratings[cite: 4].
    * [cite_start]**Features intuitive navigation** through custom buttons, enhancing user experience across different report sections[cite: 1, 2, 3, 4].
    * **Implements advanced DAX measures** to derive actionable insights, such as average classical ratings for teams and comparative player statistics.

## Technologies Used

* **Python:**
    * `selenium`: For web scraping and browser automation.
    * `pandas`: For data manipulation and analysis.
* **Power BI Desktop:** For data modeling, dashboard design, and visualization.
