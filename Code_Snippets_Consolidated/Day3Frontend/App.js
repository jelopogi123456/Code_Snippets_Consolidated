import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

const apiUrl = 'http://localhost:5000/api/v1/summarized_articles';

function App() {
  const [articles, setArticles] = useState([]);
  const [selectedArticle, setSelectedArticle] = useState(null);
  const [currentPage, setCurrentPage] = useState(1);
  const [articlesPerPage, setArticlesPerPage] = useState(10);
  const [searchText, setSearchText] = useState('');

  useEffect(() => {
    const fetchArticles = async () => {
      const params = {
        title: searchText,
        author: searchText,
        date: searchText,
        source: searchText
      };
      const response = await axios.get(apiUrl, { params });
      setArticles(response.data);
    };
    fetchArticles();
  }, []);

  const indexOfLastArticle = currentPage * articlesPerPage;
  const indexOfFirstArticle = indexOfLastArticle - articlesPerPage;
  const currentArticles = articles.slice(indexOfFirstArticle, indexOfLastArticle);

  const paginate = (pageNumber) => setCurrentPage(pageNumber);

  const handleSearch = (event) => {
    setSearchText(event.target.value);
  };

  const filteredArticles = currentArticles.filter((article) =>
    article.summarized_articles.toLowerCase().includes(searchText.toLowerCase())
  );

  return (
    <div className="App">
      <h1>Summarized Articles</h1>
      <input
        type="text"
        placeholder="Search articles"
        value={searchText}
        onChange={handleSearch}
      />
      {selectedArticle ? (
        <DetailedView article={selectedArticle} setSelectedArticle={setSelectedArticle} />
      ) : (
        <>
          <ArticleList articles={filteredArticles} setSelectedArticle={setSelectedArticle} />
          <Pagination
            articlesPerPage={articlesPerPage}
            totalArticles={articles.length}
            paginate={paginate}
          />
        </>
      )}
    </div>
  );
}

const ArticleList = ({ articles, setSelectedArticle }) => (
  <ul className="article-list">
    {articles.map((article, index) => (
      <li key={index}>
        <a
          href="#"
          onClick={(e) => {
            e.preventDefault();
            setSelectedArticle(article);
          }}
        >
          <h3>{article.title}</h3>
          <p>{article.author} - {article.date} - {article.source}</p>
        </a>
      </li>
    ))}
  </ul>
);
const DetailedView = ({ article, setSelectedArticle }) => (
  <div className="detailed-view">
    <h2>{article.title}</h2>
    <p>{article.author} - {article.date}</p>
    <p>{article.summarized_articles}</p>
    <a href={article.source} target="_blank" rel="noreferrer">Read the original article</a>
    <button onClick={() => setSelectedArticle(null)}>Back to list</button>
  </div>
);

const Pagination = ({ articlesPerPage, totalArticles, paginate }) => {
  const pageNumbers = [];

  for (let i = 1; i <= Math.ceil(totalArticles / articlesPerPage); i++) {
    pageNumbers.push(i);
  }

  return (
    <nav>
      <ul className="pagination">
        {pageNumbers.map((number) => (
          <li key={number} className="page-item">
            <a onClick={() => paginate(number)} href="#!" className="page-link">
              {number}
            </a>
          </li>
        ))}
      </ul>
    </nav>
  );
};

export default App;
