<template>
    <div id="article">
        <div class="card mb-4 mx-auto" style="max-width: 50%; ">
            <div class="row no-gutters">
                <h2 class="card-title mx-auto"> <strong> {{n.title}} </strong></h2>
                <p class="card-text mx-auto"><small class="text-muted"> {{n.date_time}} {{n.author}} </small></p>
                <div class="card-body">
                    <img :src="n.image_source" class="card-img">
                    <p class="card-text"> {{n.content}} </p>
                    <div class="embed-responsive embed-responsive-16by9" v-if="n.video_source !== null">
                        <iframe class="embed-responsive-item" :src="n.video_source" ></iframe>
                    </div>
                </div>    
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'NewsArticle',
    props: ['news_article'],
    data() {
    return {
        n: this.news_article
    }
  }
}
</script>
