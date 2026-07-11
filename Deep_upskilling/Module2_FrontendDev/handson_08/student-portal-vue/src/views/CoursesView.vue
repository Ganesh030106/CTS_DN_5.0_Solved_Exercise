<template>

<div class="container">

  <h2>Courses</h2>

  <input
    v-model="searchTerm"
    placeholder="Search Course"
  >

  <p v-if="loading">
    Loading Courses...
  </p>

  <div
    v-for="course in filteredCourses"
    :key="course.id"
    class="course-card">

    <h3>
      {{ course.title }}
    </h3>

    <p>
      {{ course.body }}
    </p>

  </div>

  <p v-if="
      !loading &&
      filteredCourses.length === 0
    ">

    No courses found

  </p>

</div>

</template>

<script setup>

import { ref, computed, onMounted } from 'vue'

import { getCourses }
from '../services/courseService'

const courses = ref([])

const searchTerm = ref('')

const loading = ref(false)

onMounted(async () => {

  loading.value = true

  try {

    const response =
      await getCourses()

    console.log(response.data)

    courses.value =
      response.data

  }

  catch(error) {

    console.error(
      'API Error:',
      error
    )

  }

  finally {

    loading.value = false

  }

})

const filteredCourses = computed(() =>
  courses.value.filter(course =>
    course.title
      .toLowerCase()
      .includes(searchTerm.value.toLowerCase())
  )
)

</script>

<style scoped>

.container {
  max-width: 1000px;
  margin: 20px auto;
}

input {
  width: 100%;
  padding: 10px;
  margin-bottom: 20px;
}

.course-card {
  background: white;

  padding: 15px;

  margin-bottom: 15px;

  border-radius: 8px;

  box-shadow:
    0 2px 5px
    rgba(0,0,0,0.1);
}

</style>