# Chess Player Data Scraper & Analyzer

## Project Overview

This project provides an end-to-end solution for collecting, processing, and visualizing comprehensive chess player data. It leverages Python for web scraping and data preparation, followed by Power BI for creating an interactive and insightful dashboard. The goal is to provide a clear overview of chess player statistics, including ratings, rankings, and geographical distribution, for various formats (Classical, Rapid, Blitz).

## Features

* **Automated Web Scraping:**
    * **Extracts** chess player names, titles (GM, IM, etc.), countries, and their Classical, Rapid, and Blitz ratings from `chess.com/ratings`.
    * **Handles pagination** to collect data across multiple pages.
    * **Cleans and preprocesses** raw scraped data to ensure accuracy and consistency.

* **Data Preparation & Storage:**
    * Uses **Pandas** for efficient data manipulation and structuring.
    * Exports the processed data into a clean **CSV file**, ready for consumption by analytical tools.

* **Interactive Power BI Dashboard:**
    * **Visualizes key metrics** such as total players, grandmasters, international masters, and distribution across countries.
    * **Provides detailed player information**, including individual ratings and world/national ranks.
    * **Showcases top 10 players** for Classical, Rapid, and Blitz formats.
    * **Displays national team compositions** and average ratings.
    * **Features intuitive navigation** through custom buttons, enhancing user experience.
    * **Utilizes advanced DAX measures** for dynamic calculations and deeper insights.

## Technologies Used

* **Python:**
    * `selenium`: For web scraping and browser automation.
    * `pandas`: For data manipulation and analysis.
* **Power BI Desktop:** For data modeling, dashboard design, and visualization.
* **Git/GitHub:** For version control and project hosting.

## Setup and How to Run

### 1. Web Scraping (Python)

To run the web scraping script:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourUsername/Chess-Player-Data-Scraper-Analyzer.git](https://github.com/YourUsername/Chess-Player-Data-Scraper-Analyzer.git)
    cd Chess-Player-Data-Scraper-Analyzer
    ```
    *(Replace `YourUsername` with your actual GitHub username)*

2.  **Install Python dependencies:**
    ```bash
    pip install selenium pandas
    ```

3.  **Download WebDriver:**
    * This script uses `webdriver.Chrome()`. You need to download the appropriate `chromedriver` executable for your Chrome browser version.
    * Place the `chromedriver.exe` (or `chromedriver` for macOS/Linux) in your system's PATH, or in the same directory as your `main.py` script.
    * You can download `chromedriver` from [here](https://chromedriver.chromium.org/downloads).

4.  **Run the Python script:**
    ```bash
    python main.py
    ```
    This will open a Chrome browser window (controlled by Selenium), navigate through the chess.com ratings pages, scrape the data, and then save it as `chess_ratings.csv` in the project directory.

### 2. Power BI Dashboard

To view and interact with the Power BI dashboard:

1.  **Ensure you have Power BI Desktop installed.** You can download it for free from the [Microsoft Power BI website](https://powerbi.microsoft.com/desktop/).
2.  **Open the `.pbix` file** (e.g., `Chess_Ratings_Dashboard.pbix`) provided in this repository using Power BI Desktop.
    * *(Note: The `.pbix` file is not included in the prompt, but would typically be part of a full GitHub repository for this project.)*
3.  The dashboard should load, displaying the visualizations and interactive elements.

## Usage

Once the Power BI dashboard is open:

* **Navigate:** Use the green navigation buttons on the left (`Overview`, `Player Info`, `Top 10`, `Teams`) to switch between different sections of the report.
* **Explore Player Info:** On the "Player Info" page, you can select a specific player (if enabled in your dashboard) to view their detailed ratings and ranks.
* **Filter Data:** Utilize any slicers or filters present on the dashboard to narrow down the data by country, title, or other criteria.
* **Hover for Details:** Hover over visuals to see tooltips with additional information.

## Output Example

The `main.py` script generates a `chess_ratings.csv` file, which will contain columns similar to:
`Name`, `Title`, `Country`, `Classical Rating`, `Rapid Rating`, `Blitz Rating`.

The Power BI dashboard provides visual insights based on this data, as demonstrated in the `Chess.pdf` export you provided.

## Future Enhancements (Optional Ideas)

* **Error Handling:** Implement more robust error handling in the scraping script (e.g., for network issues, page structure changes).
* **Scheduling:** Integrate the Python script with a scheduler (e.g., cron job, Windows Task Scheduler, or cloud functions) to automate daily/weekly data updates.
* **Database Integration:** Instead of CSV, store the data directly into a database (e.g., SQLite, PostgreSQL) for more scalable storage and querying.
* **Advanced Analytics:** Incorporate more complex analytical models or predictions within Power BI using its AI capabilities or integrating with R/Python scripts.
* **User Interface for Scraper:** Create a simple GUI for the Python scraper to make it more user-friendly.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details. *(You would need to create a `LICENSE` file in your repository)*

---

Feel free to customize the sections and add more specific details that highlight your unique contributions and the strengths of your project! Remember to include your `.pbix` file in the GitHub repository (or provide instructions on how to recreate it if the raw data is sufficient).
