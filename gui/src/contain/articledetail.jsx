import React from "react";
import axios from "axios";
import { Card } from "antd";

const { Meta } = Card;

class ArticleDetail extends React.Component {
  state = {
    article: {}
  };

  //axios.get
  componentDidMount() {
    const articleID = this.props.match.params.articleID;
    //140.114.79.94
    axios.get(`http://127.0.0.1:8000/api/article/${articleID}`).then(res => {
      res.data["time"] =
        res.data.time.slice(0, 4) +
        "-" +
        res.data.time.slice(4, 6) +
        "-" +
        res.data.time.slice(6, 8) +
        " " +
        res.data.time.slice(8, 10) +
        ":" +
        res.data.time.slice(10, 12);

      this.setState({
        article: res.data
      });
    });
  }

  render() {
    return (
      <div>
        <Card
          hoverable
          style={{ width: 800 }}
          cover={<img alt="" src={this.state.article.img} />}
        >
          <div className="title" style={{ fontSize: 30 }}>
            {this.state.article.title}
          </div>
          <br />
          <div className="title">{this.state.article.time}</div>
          <br />
          <hr />
          <Meta
            description={this.state.article.content}
            style={{ fontSize: 18, width: 700, lineHeight: 2 }}
          />
        </Card>
      </div>
    );
  }
}

export default ArticleDetail;
