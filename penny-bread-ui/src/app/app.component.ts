import { Component } from '@angular/core';
import { SearchComponent } from './pages/search/search.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [SearchComponent],
  templateUrl: './app.component.html'
})
export class AppComponent {
  isDark = false;

  toggleDark()
  {
    this.isDark = !this.isDark;

    if(this.isDark == true)
    {
      
    }
  }
}


