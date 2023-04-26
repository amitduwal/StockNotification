<h2>Introduction </h2>

Stock market trading is a popular method of investing money in the stock market to make a profit. The stock market is known for its volatility and fluctuations in price, and investors need to keep track of the stock prices to make informed decisions. In this project, we have developed a web application that tracks the stock prices of various companies and alerts the user if the price exceeds a certain threshold.

The application uses Flask, a popular web framework for Python, to develop the server-side code. The front-end of the application is developed using HTML, CSS, and JavaScript. The application makes use of an API provided by yahoo finance to get real-time stock prices of various companies. The user can choose the company they want to track, set a threshold price, and choose the type of alert they want to receive.

<h2>Requirements</h2>

To run the Stock Price Checker, you will need the following:

•	Python 3.6 or later

•	Flask

•	yfinance

•	SMTP

•	Twilio

<h2>Features </h2>

• Real-time Stock Price Retrieval

• User-friendly Web Interface

• Notification System

<h2> Project Description </h2>

The project consists of three files: main.py, home.html, and result.html.

main.py is the main Python file that contains the server-side code for the application. It imports the necessary libraries such as Flask, requests, and os. It defines two routes: / and /result.

The / route is the home page of the application. It renders the home.html file that contains the HTML and CSS code for the home page. The home page contains a form that allows the user to select the company they want to track, set a threshold price, and choose the type of alert they want to receive. The form submits a POST request to the server with the user's selections.

The /result route is the page that displays the real-time stock price of the selected company. It renders the result.html file that contains the HTML and JavaScript code for the result page. The page uses JavaScript to periodically update the stock price and check if it exceeds the threshold price set by the user. If the price exceeds the threshold, the user is alerted via email or text message.

home.html is the HTML and CSS code for the home page of the application. It contains a form that allows the user to select the company they want to track, set a threshold price, and choose the type of alert they want to receive. The form has three input fields: stock_symbol, price_threshold, and notification_type. The stock_symbol field allows the user to select the company they want to track from a dropdown list. The price_threshold field allows the user to set a threshold price for the selected company. The notification_type field allows the user to choose whether they want to receive an alert via email or text message.

result.html is the HTML and JavaScript code for the result page of the application. It displays the real-time stock price of the selected company and periodically updates the price using JavaScript. If the price exceeds the threshold set by the user, the user is alerted via email or text message. The page uses AJAX to communicate with the server and retrieve the real-time stock price of the selected company.

<h2>Usage</h2>
•	Clone the repository to your local machine:

> git clone https://github.com/your_username/stock-price-checker.git

•	Navigate to the project directory:
cd stock-price-checker

•	Run the Flask application:
python app.py

•	Open your web browser and go to http://localhost:5000.

•	Enter the ticker symbol of the company whose stock price you want to check.

•	Press the "Check Price" button to retrieve the current stock price of the company.

•	To receive email or text notifications, enter your email address or phone number in the respective fields and press "Notify Me".

•	You will receive notifications when the stock price of the company you are tracking exceeds the threshold you set.


![working](https://clipchamp.com/watch/njBSbjR36iC)
