import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { CourseService }
  from '../services/course.service';

@Component({
  selector: 'app-course-list',
  standalone: true,

  imports: [
    CommonModule,
    FormsModule
  ],

  templateUrl: './course-list.html'
})
export class CourseList implements OnInit {

  courses: any[] = [];

  loading = false;

  searchTerm = '';

  constructor(
    private courseService: CourseService
  ) { }

  ngOnInit(): void {

    this.loading = true;

    setTimeout(() => {
      console.log(this.courses);
    }, 2000);

    this.courseService.getCourses().subscribe({
      next: (data) => {

        console.log('API DATA:', data);

        this.courses = [...data];

        this.loading = false;

        console.log('Loading:', this.loading);
        console.log('Courses:', this.courses);
      },

      error: (error) => {

        console.error(error);

        this.loading = false;
      }
    });
  }

  get filteredCourses() {

    return this.courses.filter(course =>
      course.title
        .toLowerCase()
        .includes(this.searchTerm.toLowerCase())
    );
  }
}