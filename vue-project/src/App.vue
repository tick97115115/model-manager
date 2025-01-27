<template>
  <v-layout>
    <v-navigation-drawer expand-on-hover rail color="#42b883"
      ><v-list density="compact" nav>
        <v-list-item
          prepend-icon="mdi-cards"
          title="Models"
          value="models"
        ></v-list-item>
        <v-list-item
          prepend-icon="mdi-eye-outline"
          title="AI Image Tagger"
          value="ai-image-tagger"
        ></v-list-item>
        <v-list-item
          prepend-icon="mdi-image-search"
          title="Image Info"
          value="image-info"
        ></v-list-item>
        <v-list-item
          prepend-icon="mdi-cog"
          title="Settings"
          value="settings"
        ></v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <Models></Models>
    </v-main>
  </v-layout>
</template>

<script setup lang="ts">
import Models from "./views/Models.vue";
</script>

<style lang="postcss" module="header">
.root {
  color: red;
}
</style>
