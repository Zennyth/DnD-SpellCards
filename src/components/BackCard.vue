<template>
  <div class="back-card">
    <img class="back-card-img" src="@/assets/back/crest.png" alt="">
  </div>
</template>

<script>
export default {
  props: {
    spell: Object
  },
  computed: {
  }
}
</script>

<style lang="scss">
.back-card {
  width: 70mm;
  height: 120mm;
  position: relative;
  background: #ffffff;

  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  border: .5px solid black;

  &-img {
    height: calc(120mm);
  }
}
</style>
