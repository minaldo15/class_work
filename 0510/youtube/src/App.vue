<template>
  <div class="container">
    <h1 class="display-4">SSAFY TUBE</h1>
    <div class="row mt-4">
      <div class="col-12">
        <h2>{{ videoTitle }}</h2>
        <div class="embed-responsive embed-responsive-16by9">
          <iframe class="embed-responsive-item" :src="videoUrl" allowfullscreen></iframe>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Vue from 'vue';
import axios from 'axios';
import VueYoutube from 'vue-youtube';

export default {
  name: 'App',
  data() {
    return {
      videoUrl: '',
      videoTitle: ''
    }
  },
  created() {
    const searchQuery = '코딩 노래';
    const encodedQuery = encodeURIComponent(searchQuery);
    axios.get(`https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q=${encodedQuery}&type=video&key=${process.env.VUE_APP_YOUTUBE_API_KEY}`)
      .then(response => {
        const videoId = response.data.items[0].id.videoId;
        this.videoUrl = `https://www.youtube.com/embed/${videoId}`;
        this.videoTitle = response.data.items[0].snippet.title;
      })
      .catch(error => {
        console.log(error);
      })
  },
  mounted() {
    Vue.use(VueYoutube);
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
