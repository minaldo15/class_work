<template>
  <div class="about">
    <h1>로또</h1>
    <button @click="getLottoNumber" class="btn btn-success">Get Lucky Numbers</button>
    <p><input v-bind:value="number" class="Input" type="text" disabled></p>
  </div>
</template>

<script>
import _ from 'lodash';
export default {
  data() {
    return {
      number: ""
    }
  },
  methods: {
    getLottoNumber() {
      this.number = " "
      for (let i=0; i<6; i++) {
        this.number += (String(_.sample(_.range(1,46))) + " ")
      } + " ]"
    }
  }
}
</script>