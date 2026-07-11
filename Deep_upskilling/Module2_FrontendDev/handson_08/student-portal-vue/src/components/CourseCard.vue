<template>
  <div class="course-card">

    <h3>{{ name }}</h3>

    <p>Code: {{ code }}</p>

    <p>Credits: {{ credits }}</p>

    <p>Grade: {{ grade }}</p>

  </div>
</template>

<script setup>

defineProps({
  name: String,
  code: String,
  credits: Number,
  grade: String
})

</script>

<style scoped>

.course-card {
  background: white;
  border-radius: 8px;
  padding: 15px;
  margin-bottom: 15px;

  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

</style>