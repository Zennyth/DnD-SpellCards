<template>
  <div class="card">
    <div class="card-lvl" v-if="abrv != ''">
      <h1>{{spell.lvl}}</h1>
      <h3>{{abrv}}</h3>
    </div>
    <div class="card-body">
      <div class="card-body__title">
        <h1>{{spell.title}}</h1>
        <h3>{{spell.class}}</h3>
      </div>
      <div class="card-body__properties">
        <div class="wrapper" v-for="property in spell.properties" :key="property.name">
          <h3>{{property.name}}</h3>
          <h3>{{property.value}}</h3>
        </div>
      </div>
      <div class="card-body__dices">
        <img src="@/assets/dices.jpg" alt="">
      </div>
      <div class="card-body__description">
        <p v-for="(p, index) in spell.description" :key="index">{{p}}</p>
      </div>
      <div class="card-body__higher-levels" v-if="spell['higher-levels'].length > 0">
        <h3>Aux niveaux supérieurs</h3>
        <p v-for="(p, index) in spell['higher-levels']" :key="index">{{p}}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    spell: Object
  },
  computed: {
    abrv: function() {
      switch(this.spell.lvl) {
        case 0:
          return ""
        case 1:
          return "er"
        case 2:
          return "nd"
        default:
          return "ème"
      }
    }
  }
}
</script>

<style lang="scss">
.card {
  width: 70mm;
  height: 120mm;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  border: .5px solid black;
  position: relative;
  background: #ffffff;

  h1 {
    font-size: 1.75em;
  }
  h3 {
    font-size: smaller;
  }
  p {
    font-size: .585em;
    text-align: left;
  }

  &-lvl {
    position: absolute;
    top: 0.5em;
    left: 0.5em;
    background: #ffffff;
    display: flex;
    justify-content: center;
    padding-right: .25em;
    z-index: 0;

    h3 {
      text-transform: uppercase;
    }
  }

  &-body {
    border: 1px solid #D4D4D4;
    height: calc(120mm - 2.5em);
    padding: 0 .4em;
    padding-top: .25em;
    margin: 1em;
    overflow: hidden;

    > div {
      z-index: 1;
      position: relative;
      margin-top: .5em;
    }

    h1 {
      font-size: 1.25em;
    }
    h3 {
      font-size: .75em;
    }

    &__title {
      h1 {
        font-family: 'Magical';
        font-size: 2.25em;
        text-transform: capitalize;
      }
      h3 {
        text-transform: uppercase;
      }
    }

    &__properties {
      width: 100%;

      .wrapper {
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: .75em;
        border-bottom: 1px dotted #D4D4D4;
      }
    }

    &__dices {
      img {
        width: 50%;
      }
    }

    &__description {
      p {
        margin-bottom: .5em;
      }
    }

    &__higher-levels {
      h3 {
        text-align: left;
      }
    }
  }
}
</style>
