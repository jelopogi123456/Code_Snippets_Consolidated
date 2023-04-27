##Summarized Articles App
#Overview
The front-end UI code is built with React, a popular JavaScript library for building user interfaces. The code consists of a single App component, which contains three child components: ArticleList, DetailedView, and Pagination.

The ArticleList component is responsible for rendering a list of summarized articles, while the DetailedView component displays a detailed view of a single article. The Pagination component provides navigation between pages of articles.

The UI also includes a search bar that allows users to search for articles by keywords.

#App Component
The App component is the root component of the UI. It defines the state of the UI, including the list of articles, the currently selected article, the current page number, the number of articles to display per page, and the search text.

The useEffect hook is used to fetch the list of articles from the REST API when the component mounts. The paginate function is used to update the current page number when the user clicks on a page number in the pagination bar.

The handleSearch function is called whenever the user types in the search bar, and updates the search text state accordingly.

#ArticleList Component
The ArticleList component is responsible for rendering a list of summarized articles. It takes in a list of articles and a function to handle selecting an article, and maps over the list to render each article.

Each article is rendered in a list item, with a link to the detailed view of the article. The link is generated using the setSelectedArticle function, which sets the selected article state to the current article when the link is clicked.

#DetailedView Component
The DetailedView component is responsible for displaying a detailed view of a single article. It takes in an article object and a function to handle deselecting the article, and renders the title, author, date, and summary of the article.

The component also includes a link to the original source of the article, and a button to go back to the article list.

#Pagination Component
The Pagination component is responsible for rendering a pagination bar. It takes in the number of articles to display per page, the total number of articles, and a function to handle pagination.

The component calculates the number of pages based on the number of articles and the articles per page, and maps over the pages to render each page number as a link. The link is generated using the paginate function, which sets the current page state to the current page number when the link is clicked.

#Conclusion
Overall, the front-end UI code provides a simple and intuitive user interface for displaying and navigating a list of summarized articles. The code is modular and easy to maintain, with separate components responsible for specific tasks. The use of React allows for efficient rendering and easy state management.

#Installation
1.) Clone this repository to your local machine.
2.) Install Node.js and Python 3.
3.) Open a terminal or command prompt and navigate to the cloned repository.
4.) Install the required Node.js packages by running npm install.
5.) Create a virtual environment for the Flask back-end by running python -m venv venv.
6.) Activate the virtual environment by running venv\Scripts\activate on Windows or source venv/bin/activate on Unix-based systems.
7,) Install the required Python packages by running pip install -r requirements.txt.

#Usage
1.)Ensure the virtual environment is activated.
2.)Start the Flask back-end by running python RestApiTest.py from the root directory of the repository.
3.)In a separate terminal or command prompt, navigate to the root directory of the repository.
4.) Start the React front-end by running npm start.
Open a web browser and navigate to http://localhost:3000 to view the app.
