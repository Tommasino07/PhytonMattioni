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

  images = [
    'Archers.png',
    'Arrows.png',
    'Baby Dragon.png',
    'Balloon.png',
    'Barbarian Hut.png',
    'Barbarians.png',
    'Bomb Tower.png',
    'Bomber.png',
    'Bowler.png',
    'Cannon.png',
    'Clone.png',
    'Dark Prince.png',
    'Electro Wizard.png',
    'Elite Barbarians.png',
    'Elixir Collector.png',
    'Fire Spirits.png',
    'Fireball.png',
    'Freeze.png',
    'Furnace.png',
    'Giant.png',
    'Giant Skeleton.png',
    'Goblin Barrel.png',
    'Goblin Hut.png',
    'Goblins.png',
    'Golem.png',
    'Graveyard.png',
    'Guards.png',
    'Hog Rider.png',
    'Ice Golem.png',
    'Ice Spirit.png',
    'Ice Wizard.png',
    'Inferno Dragon.png',
    'Inferno Tower.png',
    'Knight.png',
    'Lava Hound.png',
    'Lightning.png',
    'Lumberjack.png',
    'Mega Minion.png',
    'Miner.png',
    'Mini P.E.K.K.A..png',
    'Minion Horde.png',
    'Minions.png',
    'Mortar.png',
    'Musketeer.png',
    'P.E.K.K.A..png',
    'Poison.png',
    'Prince.png',
    'Princess.png',
    'Rage.png',
    'Rocket.png',
    'Royal Giant.png',
    'Skeleton Army.png',
    'Skeletons.png',
    'Sparky.png',
    'Spear Goblins.png',
    'Tesla.png',
    'The Log.png',
    'Three Musketeers.png',
    'Tombstone.png',
    'Tornado.png',
    'Valkyrie.png',
    'Witch.png',
    'Wizard.png',
    'X-Bow.png',
    'Zap.png'
  ];

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
