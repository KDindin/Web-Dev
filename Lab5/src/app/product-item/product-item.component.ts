import {Component, EventEmitter, Input, Output} from '@angular/core';
import {Product, products} from "../products";

@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent {

  @Input() product: Product | undefined;
  @Output() removeID = new EventEmitter();

  isPressed: boolean = false


  share() {
    window.alert('The product has been shared!');
  }

  delete(productID: number) {
    this.removeID.emit(productID)
  }

  // pressLike() {
  //   if (this.product !== undefined) {
  //     (!this.isPressed ? this.product.likes++ : this.product.likes--)
  //     this.isPressed = !this.isPressed
  //   }
  // }
  like(product: Product) {
    product.likes += 1;
  }
}
