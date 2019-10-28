import React from "react";
import axios from "axios";
import { Card } from "antd";
import { Link, withRouter } from "react-router-dom";
class Home extends React.Component {
  state = {
    article1: {},
    article2: {},
    article3: {}
  };

  //axios.get
  componentDidMount() {
    //140.114.79.94
    axios.get(`http://127.0.0.1:8000/api/article/`).then(res => {
      var data = res.data.sort((a, b) => {
        return parseInt(b.time) - parseInt(a.time);
      });

      this.setState({
        article1: data[0],
        article2: data[1],
        article3: data[2]
      });
    });
  }

  render() {
    return (
      <div>
        <h1 style={{ fontSize: 50 }}>焦點新聞</h1>
        <Card
          hoverable
          style={{ width: 1000 }}
          cover={<img alt="" src={this.state.article1.img} />}
        >
          <div className="title" style={{ fontSize: 30 }}>
            <Link to={"/news/" + this.state.article1.id}>
              {" "}
              {this.state.article1.title}
            </Link>
          </div>
          <br />
        </Card>
        <Card
          hoverable
          style={{ width: 1000 }}
          cover={<img alt="" src={this.state.article2.img} />}
        >
          <div className="title" style={{ fontSize: 30 }}>
            <Link to={"/news/" + this.state.article2.id}>
              {this.state.article2.title}{" "}
            </Link>
          </div>
          <br />
        </Card>
        <Card
          hoverable
          style={{ width: 1000 }}
          cover={<img alt="" src={this.state.article3.img} />}
        >
          <div className="title" style={{ fontSize: 30 }}>
            <Link to={"/news/" + this.state.article3.id}>
              {this.state.article3.title}
            </Link>
          </div>
          <br />
        </Card>
      </div>
    );
  }
}

export default withRouter(Home);
