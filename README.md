# Sports Betting with Arbitrage and Fixtures Data


**Part 1:**

<p align="center">
  <img src="https://user-images.githubusercontent.com/113403062/190924275-629eaf18-183c-4781-81a2-fd0337143ba9.jpg" alt="animated"/>
</p>

*Above is an example of what the output Excel file may look like.*

In this part of the project I use **Live Sports Odds API (https://the-odds-api.com/)**. This site provides statistical arbitrage opportunities in upcoming sporting events worldwide. By leveraging real-time odds data from various bookmakers, the program aims to uncover distinct odds offered by different books and exploit them for potential profit.

Arbitrage opportunities arise when a bettor strategically places specific bets with different bookmakers, allowing them to hedge their positions and guarantee a profit. To achieve this, the program focuses on the eight nearest upcoming sporting events and analyzes the odds provided by the Live Sports Odds API.

Once the program identifies these opportunities, it performs calculations to determine the expected earnings associated with each opportunity. The findings are then compiled into a comprehensive Excel file, which includes key information such as the ID and Sport Key (specific metrics provided by the Live Sports Odds API). Additionally, the file presents details such as the Expected Earnings, Bookmaker, Name, Odds, and Amount to Buy for each respective bet, providing users with a clear overview of the identified arbitrage opportunities.

You can find all the code for this program in the **Scraper.ipynb** file. Each code chunk is accompanied by comments to provide a clear understanding of each step in the program's execution. It's important to note that the API does not update instantaneously, and bookmakers frequently adjust their odds to minimize arbitrage opportunities for bettors. As a result, there might be instances where the program outputs slightly inaccurate odds due to the odds already being updated on the bookmaker's website.

For your convenience, the **Books.txt** file contains a comprehensive list of US bookmakers supported by the Live Sports Odds API as of 3/17/22. You can also refer to the API's documentation website mentioned above for this information.

Lastly, in order to use this project, you will need to acquire an API key from the website linked above. 



**Part 2:**


<p align="center">
  <img src="https://github.com/guilhermedcampos/arbitrage-sports-betting/assets/110358692/a4e95448-aed1-4b66-8907-c76ed178c15e" alt="animated"/>
</p>

*Above is an example of what the output in the terminal may look like.*

In this phase of the project, I utilized the **Club ELO API (https://clubelo.com/API/)** to retrieve data about football clubs and upcoming fixtures through API requests. The program generates a table of outcomes for each game, providing win, lose, and draw percentages. It also identifies the most likely outcome for each match based on the gathered data.

Additionally, the program collects historical performance data for each team, including their last five matches. This information allows for a comprehensive evaluation of their recent performances.

For a clear understanding of each step in the code's execution, you can review the implementation in the **OutcomesScraper.ipynb**, which includes explanatory comments. Please note that due to incomplete data tables or API request limitations from the site, there may be instances where the program fails to output certain data. 

It's also possible to retrieve data from just one specific game, as explained in the file.
