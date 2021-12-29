<template>
  <div id="sheet">
    <Card v-for="spell in spells" :key="spell.title" :spell="spell"/>
  </div>
</template>

<script>
import Card from './components/Card.vue';
import spells from './assets/spells/example.json';

export default {
  name: 'App',
  components: {
    Card
  },
  data: () => {
    return {
      spells: spells
    }
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
}

@font-face {
  font-family: "Magical";
  src: local("fonts"), url(./assets/fonts/MagicSchoolOne-ovYz.ttf) format("truetype");
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background: #f0f0f0;
  display: flex;
  justify-content: center;
}

#sheet {
  width: 210mm;
  height: 297mm;
  background: #ffffff;
  margin: 1em;
  display: flex;
  flex-wrap: wrap;
}

@media print {
  #sheet {
    margin: 0;
  }
}

</style>
