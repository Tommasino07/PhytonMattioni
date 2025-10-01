import { HttpClient } from '@angular/common/http';
import { Component, OnInit, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App implements OnInit {
  protected readonly title = signal('clientTest');
  data: any;

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.getHello().subscribe({
      next: (data: any) => {console.log('Risposta dal server:', data); this.data  = data;},
      error: (err: any) => console.error('Errore nella richiesta HTTP:', err)
    });
  }

  getHello(): Observable<string> {
    return this.http.get('https://stunning-space-potato-699jjrp95q7pc44jx-5000.app.github.dev/', { responseType: 'text' });
  }
}
