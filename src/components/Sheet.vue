<template>
  <div class="sheet">
    <FrontCard v-for="spell in spells" :key="spell.title" :spell="spell"/>
  </div>
  <div class="sheet">
    <BackCard v-for="spell in spells" :key="spell.title" :spell="spell"/>
  </div>
</template>

<script>
import FrontCard from './FrontCard.vue';
import BackCard from './BackCard.vue';

export default {
  components: {
    FrontCard,
    BackCard
  },
  props: {
    spells: Array
  },
  computed: {
  }
}
</script>

<style lang="scss">
.sheet {
  width: 210mm;
  height: 297mm;
  padding: 0.1em;
  background: #ffffff;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  page-break-after: always;
}
</style>
