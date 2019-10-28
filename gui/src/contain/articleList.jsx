import React from "react";
import axios from "axios";
import Article from "../component/article";

class ArticleList extends React.Component {
  state = {
    articles: []
  };

  //axios.get
  componentDidMount() {
    //140.114.79.94
    axios.get("http://127.0.0.1:8000/api/article/").then(res => {
      var data = res.data.sort((a, b) => {
        return parseInt(b.time) - parseInt(a.time);
      });

      this.setState({
        articles: data
      });
    });
  }

  render() {
    return (
      <div>
        <div style={{ fontSize: 50 }}>新聞列表</div>
        <hr />
        <Article data={this.state.articles} />
      </div>
    );
  }
}
export default ArticleList;
