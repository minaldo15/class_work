<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <button @click="getLunchMenu" class="btn btn-success">Pick Lunch</button>
    <h3>{{ lunchMenu }}</h3>

  
  </div>
</template>

<script>
export default {
  data() {
    return {
      menus: ["국밥", "라면", "피자", "돈까스", "치킨", "제육"],
      lunchMenu: "",
    }
  },
  name: 'HelloWorld',
  props: {
    msg: String
  },
  methods: {
    getLunchMenu() {
      const randomIndex = Math.floor(Math.random() * this.menus.length);
      this.lunchMenu = this.menus[randomIndex];
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
