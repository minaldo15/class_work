<template>
  <div>
    <input 
      type="text" 
      v-model="title" 
      @keyup.enter="createTodo"
    >
    <button @click="createTodo">+</button>
  </div>
</template>

<script>
import axios from'axios'
const API_URL = 'http://127.0.0.1:8000/todos/'

export default {
  name: 'CreateTodo',
  data: function () {
    return {
      title: null,
    }
  },
  methods: {
    createTodo: function () {
      const title = this.title

      if (!title) {
        alert('제목을 입력해주세요')
        return
      }
      axios({
        methods: 'post',
        url: `${API_URL}/api/v1/articles/`,
        data: {title},
      })
      .then(() => {
        this.$router.push({name: 'TodoList'})
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
}
</script>