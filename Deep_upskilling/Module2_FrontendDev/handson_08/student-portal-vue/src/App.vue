<template>

<nav>

  <router-link to="/">
    Courses
  </router-link>

  <router-link to="/profile">
    Profile
  </router-link>

</nav>

<router-view />

</template>

<style>

body {
  margin: 0;
  font-family: Arial, sans-serif;
  background: #f4f6f9;
}

nav {
  background: #1976d2;
  padding: 15px;
}

nav a {
  color: white;
  margin-right: 20px;
  text-decoration: none;
  font-weight: bold;
}

</style>