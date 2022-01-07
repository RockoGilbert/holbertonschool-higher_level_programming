#!/usr/bin/node

class Rectangle {
    constructor(x, y, width, height) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
      }

      toString (){
         return `[x = ${this.x}, y = ${this.y}, width = ${this.width}, height = ${this.height}]`
        }
    };

    let zRect = new Rectangle(2, 2, 4, 4);
    console.log(zRect.toString());
    