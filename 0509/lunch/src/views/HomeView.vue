<template>
  <div class="home">
    <HelloWorld msg="점심 메뉴"/>
    <br>
    <h2>로또를 뽑아보자</h2>
    <button @click="toAbout">Pick Lotto</button>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'HomeView',
  methods: {
    toAbout() {
      this.$router.push({ name: 'about'})
    }
  },
  components: {
    HelloWorld
  }
}
</script>
