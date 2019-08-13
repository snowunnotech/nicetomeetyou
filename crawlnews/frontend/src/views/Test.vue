<template>
  <div class="test">
    <img alt="Vue logo" src="../assets/logo.png">
    <AxiosTest msg="Welcome to Axios Test"/>
  </div>
</template>

<script>
// @ is an alias to /src
import AxiosTest from '@/components/AxiosTest.vue'

export default {
  name: 'test',
  components: {
    AxiosTest
  }
}
</script>
