import Vue from 'vue'
import Router from 'vue-router'
import ArticleListView from '@/components/ArticleList'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/', redirect: { name: 'ArticleList' }
    },
    {
      path: '/articles/',
      name: 'ArticleList',
      component: ArticleListView
    }
  ]
})
