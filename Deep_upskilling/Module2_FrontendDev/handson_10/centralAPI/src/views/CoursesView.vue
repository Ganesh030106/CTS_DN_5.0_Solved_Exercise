<template>

<h1>
Courses
</h1>

<button class="refresh-btn" @click="courseStore.fetchCourses()">
    Refresh Courses
  </button>

<button
class="reset-btn"
@click="
courseStore.resetStore()
"
>
Reset Store
</button>

<p v-if="loading">
Loading Courses...
</p>

<p
v-if="error"
class="error"
>
{{ error }}
</p>

<div
v-if="!loading"
class="course-container"
>

<div
v-for="course in courses"
:key="course.id"
class="course-card"
>

<h3>
{{ course.title }}
</h3>

<p>
Course ID:
{{ course.id }}
</p>

<button
@click="
courseStore.fetchAndEnroll(
course.id
)"
>
Enroll
</button>

</div>

</div>

</template>


<script setup>

import { onMounted }
from "vue";

import { storeToRefs }
from "pinia";

import {
  useCourseStore
}
from "../stores/courseStore";

const courseStore =
  useCourseStore();

const {
  courses,
  loading,
  error
}
=
storeToRefs(
  courseStore
);

onMounted(() => {

  courseStore.fetchCourses();

});

</script>