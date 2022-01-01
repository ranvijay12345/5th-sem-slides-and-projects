import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment as ENV } from "../../../environments/environment";

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private http: HttpClient) { }

  getAll(): Promise<any> {
    return new Promise(resolve => {
      this.http.get(`${ENV.API_URL}/user/get-all`).subscribe((response: any) => {
        if (response.error) {
          console.error(response);
          return;
        }

        resolve(response);
      });
    });
  }
}

