<template>
  <b-card :title="this.title" class="rtstat">
    <div class="wrap">
      <h1 class="display-3 adaptive" id="{{ this.data }}">
        {{ this.data }}
        <span v-on:change="" class="lead"> {{ this.unit }} </span>
      </h1>
    </div>
  </b-card>
</template>

<script>
export default {
  name: "RTStatCard",
  props: {
    data: [Number, String],
    title: String,
    unit: String
  },
  computed: {
    cssProps(){
      return {
        'background-color':
      }
    }
  }
};
</script>

<style lang="scss" scoped>
.rtstat {
  position: relative;
}

.adaptive {
  font-size: 2rem;

  @include sm {
    font-size: 2.5rem;
  }

  @include lg {
    font-size: 3.5rem;
  }
}

.wrap {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding-bottom: 1.5rem;
}

#Light {
  background-color: {{ }}
}
</style>
