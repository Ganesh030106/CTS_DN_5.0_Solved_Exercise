<template>

<div class="container">

  <h2>Student Profile</h2>

  <form @submit.prevent="submitForm">

    <div class="form-group">

      <label>Name</label>

      <input
        v-model="name"
        type="text"
      >

      <p
        class="error"
        v-if="nameTouched && !name"
      >
        Name is required
      </p>

    </div>

    <div class="form-group">

      <label>Email</label>

      <input
        v-model="email"
        type="email"
      >

      <p
        class="error"
        v-if="emailTouched && !validEmail"
      >
        Enter a valid email
      </p>

    </div>

    <div class="form-group">

      <label>Semester</label>

      <input
        v-model="semester"
        type="number"
      >

    </div>

    <button
      type="submit"
      :disabled="!isValid"
    >
      Submit
    </button>

  </form>

</div>

</template>

<script setup>

import { ref, computed, watch } from 'vue'

const name = ref('')
const email = ref('')
const semester = ref('')

const nameTouched = ref(false)
const emailTouched = ref(false)

watch(name, () => {
  nameTouched.value = true
})

watch(email, () => {
  emailTouched.value = true
})

const validEmail = computed(() =>
  /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)
)

const isValid = computed(() =>
  name.value &&
  validEmail.value &&
  semester.value
)

const submitForm = () => {

  alert('Profile Submitted Successfully')

  console.log({
    name: name.value,
    email: email.value,
    semester: semester.value
  })

}

</script>

<style scoped>

.container {
  max-width: 700px;
  margin: 30px auto;
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 8px;
  font-weight: bold;
}

input {
  width: 100%;
  padding: 10px;
}

.error {
  color: red;
  margin-top: 5px;
}

button {
  background: #1976d2;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
}

button:disabled {
  background: gray;
}

</style>