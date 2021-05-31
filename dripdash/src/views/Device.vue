<template>
  <b-container class="dashboard">
    <AtAGlance
      :glances="this.device.glances"
    />
    <b-card title="Temperature" class="span-2 h-2">
      <RTLineChart
        :fields="['waterTemp', 'airTemp']"
        :labels="['Water', 'Air']"
        :data="this.device.data"
        :average="6"
      />
    </b-card>
    <RTStat 
      :data="this.device.latest.humidity"
      title="Humidity"
      unit="%"
      class="h-1"
    />
    <RTStat 
      :data="this.device.latest.light"
      title="Light"
      unit="lux"
      class="h-1"
    />
    <RTStat 
      :data="this.device.latest.ph"
      title="pH"
      unit="pH"
      class="h-1"
    />
    <b-card title="Water Levels" class="span-2 h-2">
      <RTLineChart
        :fields="['beds[0].level', 'beds[1].level', 'beds[2].level']"
        :labels="['Bed 1', 'Bed 2', 'Bed 3']"
        :data="this.device.data"
        :average="6"
      />
    </b-card>
  </b-container>
</template>

<script>
// import Dashboard from "@/components/Dashboard.vue";
import RTStat from "@/components/RTStat.vue";
import AtAGlance from "@/components/glances/AtAGlanceCard.vue";
import RTLineChart from "@/components/RTLineChart.vue";
import gql from "graphql-tag";

export default {
  name: "device",
  metaInfo: function() {
    return {
      title: this.device.name || this.device.id
    };
  },
  components: {
    // Dashboard
    RTStat,
    AtAGlance,
    RTLineChart
  },
  data() {
    return {
      device: {
        latest: {},
        glances: [],
        data: []
      }
    }
  },
  apollo: {
    device: {
      query: gql`
        query($id: String!, $from: DateTime!) {
          device(id: $id) {
            id
            name
            glances {
              title
              text
              status
            }
            latest {
              humidity
              light
              airTemp
              waterTemp
              ph
            },
            data(from: $from) {
              id
              timestamp
              waterTemp
              airTemp
              beds {
                level
              }
            }
          }
        }
      `,
      variables() {
        return {
          id: this.$route.params.id,
          from: new Date(Date.now() - 1000 * 60 * 10)
        }
      },
      pollInterval: 2000,
      deep: true
    }
  }
};
</script>

<style scoped lang="scss">
.dashboard {
  display: grid;
  gap: 1rem;
  padding: 1rem;
  grid-template-columns: 1fr;

  @include md {
    grid-template-columns: repeat(3, 1fr);
  }
}

.span-2 {
  @include md {
    grid-column-end: span 2;
  }
}

.h-1 {
  height: 12.5rem;
}

.h-2 {
  height: 20rem;
  position: relative;
}
</style>
