import Vue from 'vue'
import Router from 'vue-router'
import News from '@/components/News'
import NewsArticle from '@/components/NewsArticle'

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/nba-news',
            name: 'NbaNews',
            component: News
        },
        {
            path: '/news-article',
            name: 'NewsArticle',
            component: NewsArticle,
            props: true
        }
    ]
})