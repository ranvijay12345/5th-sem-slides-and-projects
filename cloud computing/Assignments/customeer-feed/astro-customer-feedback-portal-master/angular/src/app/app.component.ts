import { Component } from '@angular/core';
import { UserService } from './services/user/user.service';

declare var $: any;

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'angular';
  constructor(private userService: UserService) {
    $(function () {
      $("form").submit(function () { return false; });
    })

    this.userService.getAll().then(res => {
      console.log(res)
    })
  }
}
