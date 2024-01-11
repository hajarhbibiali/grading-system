import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent  implements OnInit {
  images: string[] = [
  
    '../../../assets/img1.jpeg',
    '../../../assets/muslim child.jpeg',
    '../../../assets/img3.jpeg',
    
  ];
  currentIndex = 0;

  constructor() { }

  ngOnInit(): void {
    setInterval(() => {
      this.showNextSlide();
    }, 4000); // Change slide every 2 seconds
  }

  showNextSlide(): void {
    this.currentIndex = (this.currentIndex + 1) % this.images.length;
  }
}