<template>
  <div class="axiostest">
    <h1>{{ msg }}</h1>
    <p v-for="New in news">
       {{ New.time }}
       {{ New.title }}
       {{ New.statement }}
    </p>
    <h3>Essential Links</h3>
    <h3>Ecosystem</h3>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'axiostest',
  props: {
    msg: String
  },
  data () {
    return {
      news: null
    }
  },
  mounted () {
    axios
      .get('/API/news/?format=json')
      .then(response => (this.news = response.data))
      .catch(function (error) { // 请求失败处理
        console.log(error);
      });
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
