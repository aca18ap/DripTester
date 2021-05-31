<script>
import { Line, mixins } from "vue-chartjs";
import ta from "time-ago";
const { reactiveData } = mixins;
const _get = require("lodash/get");

export default {
  extends: Line,
  mixins: [reactiveData],
  props: {
    fields: Array,
    labels: Array,
    scale: {
      required: false,
      default: null,
      type: String
    },
    data: Array,
    average: {
      type: Number,
      required: false,
      default: 0
    }
  },
  data() {
    return {
      chartData: { datasets: this.datasets }
    };
  },
  watch: {
    datasets: function(o, n) {
      this.chartData = { datasets: n };
    }
  },
  computed: {
    getLegend() {
      return {
        display: this.fields.length > 1
      };
    },
    getScaleLabel() {
      return {
        display: this.scale ? this.scale : false,
        labelString: this.scale
      };
    },
    options() {
      return {
        //Chart.js options
        scales: {
          yAxes: [
            {
              gridLines: {
                display: true
              },
              scaleLabel: this.getScaleLabel
            }
          ],
          xAxes: [
            {
              type: "time",
              gridLines: {
                display: false
              },
              time: {
                unit: "minute",
                displayFormats: {
                  minute: "YYYY-MM-DDTHH:mm:ss.sssZ"
                },
                stepSize: 2
              },
              ticks: {
                callback: function(value) {
                  if (Date.now() - Date.parse(value) < 10000) {
                    return "now";
                  } else {
                    return ta.ago(value, true);
                  }
                }
              }
            }
          ]
        },
        legend: this.getLegend,
        responsive: true,
        maintainAspectRatio: false
      };
    },
    datasets() {
      var sets = [];
      this.fields.forEach((field, i) => {
        var data = this.data.map(d => {
          return { x: new Date(d.timestamp), y: _get(d, field)};
        });

        if (this.average > 1) {
          let sum = 0;
          let cnt = 0;
          let averagedData = []
          data.forEach(({x, y}, i) => {
            sum += y;
            cnt += 1;
            if (i % this.average == this.average - 1) {
              averagedData.push({x, y: sum / cnt});
              sum = 0;
              cnt = 0;
            }
          });

          if (cnt && sum) {
            averagedData.push({ x: data[data.length - 1].x, y: sum / cnt})
          }

          data = averagedData;
        }

        var label = this.labels[i] || "";

        var borderColor = this.$store.state.settings.chartColors[i % 5];

        sets.push({
          borderColor: borderColor,
          backgroundColor: borderColor + "4D",
          label: label,
          data: data
        });
      });

      return sets;
    }
  },
  mounted() {
    this.renderChart(this.chartData, this.options);
  }
};
</script>

<style scoped>
* {
  height: Calc(100% - 2.25rem);
}
</style>
