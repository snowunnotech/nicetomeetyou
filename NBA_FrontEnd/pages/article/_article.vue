<template>
  <section class="container">
    <div>
      <h4>{{title.toUpperCase()}}</h4>
      <h2></h2>
    </div>
  </section>
</template>

<script>
import axios from 'axios'
export default {
  async asyncData ({params}) {
    const { data } = await axios.get(`http://127.0.0.1:8000/api/news/${params.index}`)
      console.log(data)
      return { title: data }
  }
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
img
{
  display: inline-block;
  border-radius: 4px;
  border: 4px solid #3b8070;
  color: #3b8070;
  text-decoration: none;
  margin-top: 10px;
}
h4 {
  margin-top: 10px;
  color: #3b8070;
}
</style>