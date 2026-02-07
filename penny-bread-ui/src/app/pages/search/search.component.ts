import { Component } from '@angular/core';
import { CommonModule } from '@angular/common'; 
import { FormsModule } from '@angular/forms';  
import { PriceService } from '../../services/price.service';

@Component({
  selector: 'app-search',
  standalone: true,  
  imports: [CommonModule, FormsModule], 
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css'],
  providers: [PriceService]
})
export class SearchComponent {
  searchQuery = '';
  location = 'Wright State University, Ohio';
  products: any[] = [];

  constructor(private priceService: PriceService) {}

 onSearch() {
  this.priceService.searchProducts(this.searchQuery).subscribe(data => {
    console.log('API response:', data);
    this.products = data;
  });
}
}
