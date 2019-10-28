import React from "react";
import { Route } from "react-router-dom";

import ArticleList from "./contain/articleList";
import ArticleDetail from "./contain/articledetail";
import Home from "./contain/home";

//React Route 藉由Route來渲染component
//<Route exact path='路徑' component={選擇的component}>

const BaseRouter = () => (
  <div>
    <Route exact path="/" component={Home} />
    <Route exact path="/news" component={ArticleList} />
    <Route exact path="/news/:articleID" component={ArticleDetail} />
  </div>
);

export default BaseRouter;
