<template>

<div class="container">

  <h2>Courses</h2>

  <input
    v-model="searchTerm"
    placeholder="Search Course"
  >

  <CourseCard
    v-for="course in filteredCourses"
    :key="course.id"
    :name="course.name"
    :code="course.code"
    :credits="course.credits"
    :grade="course.grade"
  />

  <p v-if="filteredCourses.length === 0">
    No courses found
  </p>

</div>

</template>

<script setup>

import { ref, computed, onMounted }
from 'vue'

import CourseCard
from '../components/CourseCard.vue'

const searchTerm = ref('')

const courses = ref([])

onMounted(() => {

  courses.value = [

    {
      id: 1,
      name: 'Data Structures',
      code: 'CS101',
      credits: 4,
      grade: 'A'
    },

    {
      id: 2,
      name: 'DBMS',
      code: 'CS102',
      credits: 3,
      grade: 'A+'
    },

    {
      id: 3,
      name: 'Operating Systems',
      code: 'CS103',
      credits: 4,
      grade: 'B+'
    },

    {
      id: 4,
      name: 'Computer Networks',
      code: 'CS104',
      credits: 3,
      grade: 'A'
    },

    {
      id: 5,
      name: 'Software Engineering',
      code: 'CS105',
      credits: 4,
      grade: 'A+'
    }

  ]

})

const filteredCourses = computed(() =>
  courses.value.filter(course =>
    course.name
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

</style>