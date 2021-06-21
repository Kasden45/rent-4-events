<script>
import { Bar, mixins } from 'vue-chartjs'
const { reactiveProp } = mixins
export default {
  name: 'Chart',
  extends: Bar,
  mixins: [reactiveProp],
  props: ['options'],

  mounted () {
    this.renderChart(this.chartData, this.options)
  }
}
</script>

<style scoped>

</style>

    //   {
    // chartData: {
    //   type: Object,
    //   default: null
    // },
    // options: {
    //   type: Object,
    //   default: null
    // }
  }
