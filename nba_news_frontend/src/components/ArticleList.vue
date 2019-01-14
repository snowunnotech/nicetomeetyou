<template>
  <div class="w-100">
    <!--nav bar-->
    <b-navbar toggleable="md" type="light" variant="light">
      <b-row no-gutters class="mx-2 w-100">
        <b-col cols="4" offset="4"
               md="4" offset-md="0"
               class="text-center text-md-start">
          <b-navbar-nav>
            <b-navbar-brand tag="h1" :to="{name: 'ArticleList'}">
              NBA News
            </b-navbar-brand>
          </b-navbar-nav>
        </b-col>
      </b-row>
    </b-navbar>
    <!--tell user when new articles are available-->
    <b-alert variant="success"
             :show="showAlert"
             @dismissed="showAlert=false"
             @click="getArticles">
      <a @click="getArticles">New articles available. Click me to refresh.</a>
    </b-alert>
    <!--Collapsiable section for presenting news detail-->
    <b-collapse id="detail_collapse"
                v-model="showDetailCollapse"
                class="justify-content-start justify-content-md-end mt-2">
      <b-card :title="detailedArticle.title"
              :header="detailedArticle.authorInfo"
              bg-variant="light">
        <p class="card-text">{{detailedArticle.publishDt}}</p>
        <p class="card-text">{{detailedArticle.content}}</p>
        <b-button :href="detailedArticle.url"
                  class="card-link">
          Source
        </b-button>
        <b-button v-b-toggle.detail_collapse>Dismiss</b-button>
      </b-card>
    </b-collapse>
    <!--Table for presenting made news titles-->
    <b-row id="article-table"
           align-h="center"
           align-v="start"
           no-gutters
           class="h-100 mt-2">
      <b-col cols="12">
        <b-table :items="articles"
                 :fields="article_fields"
                 :current-page="currentTablePage"
                 :per-page="perTablePage"
                 responsive="sm"
                 striped hover>
          <template slot="title" slot-scope="row">
            <!-- if collapsed then show -->
            <a aria-controls="detail_collapse"
                :class="showDetailCollapse ? 'collapsed' : null"
                :aria-expanded="showDetailCollapse ? 'true' : 'false'"
                @click="currentArticleId=row.item.id">
              {{row.value}}
            </a>
          </template>
        </b-table>
        <b-pagination size="md"
                      align="center"
                      :total-rows="articles.length"
                      v-model="currentTablePage"
                      :per-page="perTablePage">
        </b-pagination>
      </b-col>
    </b-row>
    <!-- </div> -->
  </div>
</template>
<script>
/* eslint-disable */
export default {
name: 'ArticleListView',
    data() {
      return {
        articles: [],
        article_fields: [ 
          {key: 'publish_dt', sortable: true},
          {key: 'title', sortable: false}
        ],
        showDetailCollapse: false,
        currentArticleId: 0,
        currentTablePage: 1,
        perTablePage: 5,
        showAlert: false,
        statusInterval: 1,
        remoteArticleNum: 3,
        detailedArticle: {
          authorInfo: "",
          title: "",
          publishDt: "",
          content: "",
        },
      }
    },
    created() {
      // reload sound list after this component is mounted 
      this.getArticles();
      // check len of article list every 10 sec
      this.statusInterval = setInterval(this.checkNewArticles, 10000);
    },
    watch: {
      remoteArticleNum(value) {
        if (value > this.articles.length) {
          this.showAlert = true;
        }
      },
      articles(value) {
        if (value.length >= this.remoteArticleNum) {
          this.showAlert = false;
        }
      },
      // if click on a different article then before, get the api and show if collapsed
      currentArticleId(value) {
        this.getArticleDetail(value);
        if (!this.showDetailCollapse) {
          this.showDetailCollapse = true;
        }
      }
    },
    methods: {
      api(endpoint) {
        // we only use GET here
        var config = {
          method: 'GET',
          body: null,
          headers: {
            'content-type': 'application/json'
          }
        }
        return fetch(endpoint, config) // use fetch API to get data
          .then((response) => response.json())
          .catch((error) => console.log(error));
      },
      // get article list
      getArticles() {
        this.api(process.env.ROOT_API+"/articles/").then((articles) => {
          this.articles = articles;
        });
      },
      // get article detail
      getArticleDetail(id) {
        this.api(process.env.ROOT_API+"/articles/"+id).then((article) => {
          this.detailedArticle.authorInfo = article.author_info;
          this.detailedArticle.title = article.title;
          this.detailedArticle.publishDt = article.publish_dt;
          this.detailedArticle.content = article.content;
          this.detailedArticle.url = article.url;
        });
      },
      // check len of article list
      checkNewArticles() {
        this.api(process.env.ROOT_API+"/articles/count/").then((data) => {
          this.remoteArticleNum = parseInt(data.num);
        });
      }
    },
    beforeRouteLeave (to, from, next) {
      // make sure all timers are cleared before leave
      clearInterval(this.statusInterval);
      // dismiss the route guard
      next();
    }
  }
</script>
<style scoped>

</style>
