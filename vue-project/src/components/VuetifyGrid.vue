<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" lg="10" xl="10">
        <v-row no-gutters>
          <v-col v-for="n in 3" :key="n" cols="12" sm="4" align="center">
            <v-sheet class=""> One of three columns </v-sheet>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>
