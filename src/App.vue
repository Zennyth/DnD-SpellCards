<template>
  <div class="spells">
    <Sheet
     v-for="(chunk, index) in spellChunks" 
     :key="index"
     :spells="chunk"
    />
  </div>
</template>

<script>
import Sheet from './components/Sheet.vue';
import spells from './assets/spells/example.json';

export default {
  name: 'App',
  components: {
    Sheet
  },
  data: () => {
    return {
      spells: spells
    }
  },
  computed: {
    spellChunks: function() {
      return this.chunk(this.spells, 6);
    }
  },
  methods: {
    chunk: (array, size) => {
      return array.reduce((acc, _, i) => {
        if (i % size === 0) acc.push(array.slice(i, i + size))
        return acc
      }, []);
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

@media print {
  #sheet {
    margin: 0;
  }
  #app {
    background: #ffffff;
  }
}

</style>
