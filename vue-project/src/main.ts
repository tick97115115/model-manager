import { createApp } from "vue";
import { createPinia } from "pinia";

// Vuetify
import "vuetify/styles";
import { createVuetify } from "vuetify";
import { mdi, aliases } from "vuetify/iconsets/mdi";

import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import "@mdi/font/css/materialdesignicons.css";

import App from "./App.vue";
import router from "./router";
const vuetify = createVuetify({
  components,
  directives,
  icons: {
    defaultSet: "mdi",
    aliases,
    sets: {
      mdi,
    },
  },
});

const app = createApp(App);

app.use(createPinia());
app.use(vuetify);
app.use(router);

app.mount("#app");
