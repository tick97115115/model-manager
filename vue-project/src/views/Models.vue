<template>
  <v-bottom-navigation v-model="value" :bg-color="color" grow>
    <v-btn>
      <v-icon>mdi-harddisk</v-icon>

      <span>Local</span>
    </v-btn>

    <v-btn>
      <v-icon>mdi-cloud</v-icon>

      <span>CivitAI</span>
    </v-btn>

    <!-- <v-btn>
      <v-icon>mdi-book</v-icon>
  
      <span>Book</span>
    </v-btn>
  
    <v-btn>
      <v-icon>mdi-image</v-icon>
  
      <span>Image</span>
    </v-btn> -->
  </v-bottom-navigation>
</template>

<script>
export default {
  data: () => ({ value: 1 }),

  computed: {
    color() {
      switch (this.value) {
        case 0:
          return "blue-grey";
        case 1:
          return "blue";
        case 2:
          return "brown";
        case 3:
          return "indigo";
        default:
          return "blue-grey";
      }
    },
  },
};
</script>
