import React, { Component } from "react";

import { Layout, Menu } from "antd";
import { Link, withRouter } from "react-router-dom";

const { Header, Content, Footer } = Layout;

class CustomLayout extends Component {
  render() {
    return (
      <Layout className="layout">
        <Header>
          <div className="logo" />
          <Menu
            theme="dark"
            mode="horizontal"
            defaultSelectedKeys={["2"]}
            style={{ lineHeight: "64px" }}
          >
            <Menu.Item key="1">
              <Link to="/">HOME</Link>
            </Menu.Item>
            <Menu.Item key="2">
              <Link to="/news">NEWS</Link>
            </Menu.Item>
          </Menu>
        </Header>
        <Content style={{ padding: "0 50px" }}>
          <div style={{ background: "#fff", padding: 24, minHeight: 280 }}>
            {this.props.children}
          </div>
        </Content>
        <Footer style={{ textAlign: "center" }}></Footer>
      </Layout>
    );
  }
}

export default withRouter(CustomLayout);
