<template>
  <b-card title="Control">
    <b-alert show variant="warning"
      >Control isn't yet enabled on WaterElf devices.</b-alert
    >
    <b-form @click="doUpdate">
      <b-form-checkbox v-model="autoBed" name="check-button" disabled switch>
        Automatic Bed Control
      </b-form-checkbox>
      <div v-if="!autoBed" class="manualBed">
        <h6>Manual Control</h6>
        <b-button-group size="sm" class="block">
          <b-button variant="outline-success">Flood</b-button>
          <b-button variant="outline-danger">Drain</b-button>
        </b-button-group>
        <b-button-group size="sm" class="block">
          <b-button variant="outline-success">Flood</b-button>
          <b-button variant="outline-danger">Drain</b-button>
        </b-button-group>
        <b-button-group size="sm" class="block">
          <b-button variant="outline-success">Flood</b-button>
          <b-button variant="outline-danger">Drain</b-button>
        </b-button-group>
      </div>
    </b-form>
  </b-card>
</template>

<script>
export default {
  name: "ControlCard",
  components: {},
  data() {
    return {
      autoBed: true
    };
  },
  methods: {
    doUpdate() {
      console.log("click");
    }
  }
};
</script>

<style lang="scss" scoped>
.manualBed {
  background: var(--light);
  border-radius: 0.25rem;
  margin: 0.5em 0;
  padding: 0.5em;
}

h6 {
  margin-bottom: 0;
}

.block {
  width: 100%;
  margin-top: 0.5em;
}
</style>
