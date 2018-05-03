<template>
  <section class="container">
    <div v-for="(article, index) in nbaArticles" :key="index" class="article-nba" >
      <a class="article-title">{{article.title}}</a>
      <img :src="article.img_url" alt="" >
      <div class="article">{{article.content}}</div>
    </div>
  </section>
</template>

<script>
import axios from 'axios'
export default {
  async asyncData () {
    const { data } = await axios.get(`http://127.0.0.1:8000/api/news/`)
    return { nbaArticles: data }
  },
}
</script>

<style>
.container
{
  min-height: 100vh;
  display: flex;
  justify-content: center;
  /* align-items: center; */
  text-align: center;
}
.title
{
  font-family: "Quicksand", "Source Sans Pro", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; /* 1 */
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: #35495e;
  letter-spacing: 1px;
}
.links
{
  padding-top: 15px;
}
.article-title
{
  display: inline-block;
  text-decoration: none;
  padding: 10px 30px;
  margin: 7px;
}
.article-nba
{
  display: inline-block;
  border-radius: 4px;
  border: 1px solid #3b8070;
  color: #3b8070;
  text-decoration: none;
  padding: 10px 30px;
  margin: 7px;
}
.article-nba:hover
{
  color: #fff;
  background-color: #3b8070;
}
img
{
  display: inline-block;
  border-radius: 4px;
  border: 4px solid #3b8070;
  color: #3b8070;
  text-decoration: none;
  margin-top: 10px;
  width: 200px;
  height: 150px;
}
</style>