<template>
    <div id="nba-news">
        <div class="card mb-4 mx-auto" style="max-width: 50%; "
            v-for="n in news"
            :key="n.id"
            >
            <a @click="detail(n)" style="cursor:pointer;">
                <div class="row no-gutters">
                    <div class="col-md-4">
                        <img :src="n.image_source" class="card-img">
                    </div>
                    <div class="col-md-8">
                        <div class="card-body">
                            <h5 class="card-title"> <strong> {{n.title}} </strong></h5>
                            <p class="card-text text-truncate"> {{n.content}} </p>
                            <p class="card-text"><small class="text-muted"> {{n.date_time}} </small></p>
                        </div>
                    </div>
                </div>
            </a>
        </div>
        
        <b-pagination
            v-model="page"
            :per-page="10"
            :total-rows="total_count"
            align="center"
            @change="clickCallback">
        </b-pagination>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'News',
    data() {
        return {
            news: [],
            page: 1,
            total_count: 0,
        }
    },
    created: function() {
        axios.get('/news').then(response => {
            let tmpData = response.data.data
            let tmpMeta = response.data.meta
            this.page = tmpMeta.page
            this.total_count = tmpMeta.total_count
            tmpData.forEach(element => {
                this.news.push(element)
            });
        })
    },
    methods: {
        clickCallback: function(page) {
                let api = '/news?page=' + page
                axios.get(api).then(response => {
                let tmpData = response.data.data
                let tmpMeta = response.data.meta
                this.page = tmpMeta.page
                this.total_count = tmpMeta.total_count
                this.news = []
                tmpData.forEach(element => {
                    this.news.push(element)
                });
            })
        },
        detail: function(n) {
            this.$router.push({name:'NewsArticle', params: {'news_article': n}})
        }
    }
}
</script>
