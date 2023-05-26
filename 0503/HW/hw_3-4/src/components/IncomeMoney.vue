<template>
  <div>
    <label for="income">연봉 입력 (만원): </label>
    <input type="number" id="income" v-model="incomeInputData" @keyup.enter="incomeInput">
    <br>
    <br>
    <label for="deduction">세액감면액 (만원): </label>
    <input type="number" id="deduction" v-model="deductionInputData" @keyup.enter="deductionInput">  
    <hr>
    <h2>종합소득금액: {{incomeInputData}} 만원</h2>
    <h2>종합소득공제: (-) 150 만원</h2>
    <h2>과세표준: {{}} 만원</h2>
    <Taxrate: tax-base="taxBase" :tax-deduction="taxDeduction" />
    <hr>
  </div>
</template>

<script>
import Taxrate from './components/Taxrate.vue'

export default {
  name: 'IncomeMoney',
  components: {
    Taxrate,
  },
  data: function () {
    return {
      IncomeInputData: 0,
      deductionInputData: 0,
    }
  },
  computed: {
    taxBase() {
      const base = this.income - 1500000;
      return base > 0 ? base: 0;
    }
  }
  // props: {
  //   staticProps: String,
  //   dynamicProps: String,
  // },
  // methods: {
  //   incomeToApp: function () {
  //     this.$emit('incom-to-app', 'income Data')
  //   },
  //   incomeInput: function () {
  //     this.$emit('income-input', this.IncomeInputData)
  //     this.IncomeInputData = ""
  //   },
  //   deductionInput: function () {
  //     this.$emit('deduction-input', this.DeductionInputData)
  //     this.DeductionInputData = ""
  //   },
  // }
}
</script>

<style>

</style>